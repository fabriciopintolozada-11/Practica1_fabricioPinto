# Storefront Audit

## Descripcion

`storefront-audit` es una skill local para revisar rapidamente una tienda React/Vite. Comprueba que existan los componentes principales, valida patrones de riesgo conocidos del carrito y genera un informe Markdown con resultados y numeros de linea.

## Cuando utilizarla

Usala cuando necesites demostrar el estado de una tienda React antes de corregirla, detectar regresiones en carrito/busqueda o preparar evidencia de una revision tecnica. No reemplaza las pruebas manuales del navegador.

## Flujo

1. Recibe la ruta de la raiz del proyecto.
2. Carga las reglas desde `references/checks.json`.
3. Busca archivos y patrones definidos en esas reglas.
4. Carga `assets/report-template.md` y lo completa con los resultados.
5. Escribe el informe en `reports/storefront-audit.md` o en la ruta indicada.
6. Devuelve codigo 0 si no hay errores de ejecucion. Los hallazgos se informan como `WARN`, no hacen fallar el proceso.

## Requisitos

- Python 3.9 o superior.
- Ejecutar desde cualquier carpeta; la skill resuelve sus recursos con base en la ubicacion del propio script.
- Proyecto objetivo con archivos de texto, preferiblemente React/Vite.

## Instalacion y ejecucion

No requiere paquetes externos. Desde la raiz de este repositorio:

```bash
python .codex/skills/storefront-audit/scripts/audit_storefront.py .
```

Para elegir otro archivo de salida:

```bash
python .codex/skills/storefront-audit/scripts/audit_storefront.py . --output audit.md
```

## Entrada y resultado esperado

Entrada: `.` como ruta de un proyecto React.

Resultado: un archivo Markdown con una tabla de comprobaciones y una lista de riesgos, por ejemplo:

```text
# Storefront Audit
Proyecto: ...
Comprobaciones: 7
OK: 7 | WARN: 0 | RIESGOS: 0
```

## Manejo de errores

- Si la ruta no existe o no es una carpeta, termina con codigo 2 y explica el problema.
- Si falta `package.json`, lo marca como `WARN` y continua con los demas controles.
- Si un archivo esperado no existe, registra `WARN` en vez de detener todo el informe.

## Demostracion

Caso exitoso:

```bash
python .codex/skills/storefront-audit/scripts/audit_storefront.py . --output reports/demo-success.md
```

Caso invalido:

```bash
python .codex/skills/storefront-audit/scripts/audit_storefront.py carpeta-que-no-existe
```

El segundo comando debe mostrar un error de ruta y terminar con codigo 2.
