# Tienda Tech (ejercicio de depuración)

Esta tienda con carrito **tiene exactamente 10 errores**: algunos de lógica, otros de datos/API y otros visuales.

## Cómo ejecutarla

```bash
npm install
npm run dev
```

Abre la dirección que muestra la terminal (normalmente http://localhost:5173).

## Skill de auditoría

Este repositorio incluye la skill local `storefront-audit`, ubicada en
`.codex/skills/storefront-audit/`. Sirve para revisar automáticamente la
tienda React y detectar patrones de riesgo.

Ejecutarla desde la raíz de `prac1`:

```bash
python .codex/skills/storefront-audit/scripts/audit_storefront.py . --output reports/storefront-audit.md
```

El resultado se genera en `reports/storefront-audit.md`. La skill incluye sus
reglas en `references/checks.json`, una plantilla en `assets/report-template.md`
y documentación en `SKILL.md` y `README.md`.

Para probar una ruta inválida:

```bash
python .codex/skills/storefront-audit/scripts/audit_storefront.py carpeta-que-no-existe
```

Debe informar que la ruta no existe y terminar con código 2.

## Tu tarea

1. Usa la aplicación (busca, filtra, agrega al carrito, cambia cantidades, elimina, paga) y anota todo lo que funcione o se vea mal.
2. Encuentra la causa de cada error en el código.
3. Corrígelos. Puedes usar IA, pero debes **entender y probar** cada cambio.
4. Entrega, por cada uno de los 10 errores:
   - Qué pasaba (síntoma).
   - En qué archivo y línea estaba la causa.
   - Cómo lo corregiste.
   - El prompt que usaste con la IA y si tuviste que corregirlo.

Los datos vienen de https://dummyjson.com/products
