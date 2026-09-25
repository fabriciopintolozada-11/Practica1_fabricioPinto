#!/usr/bin/env python3
"""Audit a React storefront using rules and a report template shipped with this skill."""

import argparse
import json
import re
import sys
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
RULES_FILE = SKILL_ROOT / "references" / "checks.json"
TEMPLATE_FILE = SKILL_ROOT / "assets" / "report-template.md"


def read_text(path):
    return path.read_text(encoding="utf-8")


def first_matching_line(text, pattern):
    regex = re.compile(pattern, re.MULTILINE)
    for number, line in enumerate(text.splitlines(), 1):
        if regex.search(line):
            return number
    return None


def run_check(project, rule):
    path = project / rule["file"]
    if not path.exists():
        return "WARN", f"no existe {rule['file']}"
    try:
        line = first_matching_line(read_text(path), rule["pattern"])
    except (OSError, UnicodeDecodeError) as error:
        return "WARN", f"no se pudo leer: {error}"
    return ("OK", f"{rule['file']}:{line}") if line else ("WARN", "patron no encontrado")


def main():
    parser = argparse.ArgumentParser(description="Audita una tienda React/Vite")
    parser.add_argument("project", help="ruta de la raiz del proyecto")
    parser.add_argument("--output", default="reports/storefront-audit.md", help="archivo Markdown de salida")
    args = parser.parse_args()
    project = Path(args.project).expanduser().resolve()
    if not project.is_dir():
        print(f"ERROR: la ruta no existe o no es una carpeta: {project}", file=sys.stderr)
        return 2

    try:
        rules = json.loads(read_text(RULES_FILE))
        template = read_text(TEMPLATE_FILE)
    except (OSError, json.JSONDecodeError) as error:
        print(f"ERROR: recursos de la skill invalidos: {error}", file=sys.stderr)
        return 3

    checks = []
    for rule in rules["checks"]:
        status, detail = run_check(project, rule)
        checks.append(f"- {status} {rule['label']} ({detail})")
    risks = []
    for rule in rules["risks"]:
        path = project / rule["file"]
        if path.exists():
            line = first_matching_line(read_text(path), rule["pattern"])
            if line:
                risks.append(f"- WARN {rule['label']} ({rule['file']}:{line}): {rule['note']}")
    ok_count = sum(line.startswith("- OK") for line in checks)
    output = (template.replace("{{project}}", str(project))
              .replace("{{checks_total}}", str(len(checks)))
              .replace("{{checks_ok}}", str(ok_count))
              .replace("{{checks_warn}}", str(len(checks) - ok_count))
              .replace("{{risks_total}}", str(len(risks)))
              .replace("{{checks}}", "\n".join(checks))
              .replace("{{risks}}", "\n".join(risks) if risks else "- No se detectaron riesgos."))
    destination = Path(args.output).expanduser()
    if not destination.is_absolute():
        destination = project / destination
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(output + "\n", encoding="utf-8")
    print(f"Informe generado: {destination}")
    print(f"Comprobaciones: {len(checks)} | OK: {ok_count} | WARN: {len(checks) - ok_count} | Riesgos: {len(risks)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
