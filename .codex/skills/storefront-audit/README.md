# Storefront Audit

Skill local para auditar una tienda React/Vite antes de una demostración o
revisión de código.

## Qué hace

- Comprueba archivos y patrones esenciales de la tienda.
- Detecta cinco riesgos frecuentes del carrito y la búsqueda.
- Genera un informe Markdown con estados, rutas y números de línea.
- Continúa aunque falte un archivo esperado, marcándolo como `WARN`.
- Rechaza rutas inexistentes con código de salida 2.

## Uso rápido

Desde la raíz de `prac1`:

```bash
python .codex/skills/storefront-audit/scripts/audit_storefront.py . --output reports/storefront-audit.md
```

Requisitos: Python 3.9 o superior. No instala paquetes externos.

## Estructura

```text
storefront-audit/
├── SKILL.md
├── README.md
├── assets/report-template.md
├── references/checks.json
└── scripts/audit_storefront.py
```

El script usa directamente `references/checks.json` para las reglas y
`assets/report-template.md` para construir el resultado.

## Pruebas

Caso exitoso:

```bash
python .codex/skills/storefront-audit/scripts/audit_storefront.py . --output reports/demo-success.md
```

Caso de error:

```bash
python .codex/skills/storefront-audit/scripts/audit_storefront.py carpeta-que-no-existe
```

El informe exitoso queda en `reports/demo-success.md`. Para la presentación,
captura la terminal de cada caso, el informe generado y la estructura de
carpetas.
