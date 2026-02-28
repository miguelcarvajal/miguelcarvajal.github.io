# Repository Guidelines

## Project Structure & Module Organization
Repositorio de sitio estático con Jekyll.

- Contenido: `_posts/`, `_pages/`, `_drafts/`.
- Plantillas/UI: `_layouts/`, `_includes/`, `_sass/`, `assets/`.
- Datos: `_data/*.csv` (fuente para páginas y listados).
- Configuración raíz: `_config.yml`, `index.md`, `robots.txt`, `sitemap.*`, `CNAME`.
- Salida generada: `_site/` (no editar manualmente).

## Purpose & Editorial Voice
- Propósito: mantener una web académica/profesional clara, rigurosa y útil para docencia, investigación y divulgación.
- Tono: sobrio, preciso y verificable; evitar grandilocuencia y afirmaciones no sustentadas.
- Contenido: no inventar logros, cargos, publicaciones o fechas; usar solo información existente en el repositorio.
- UX editorial: priorizar legibilidad, jerarquía clara de títulos y consistencia en español estándar.

## Build, Test, and Development Commands
- `bundle exec jekyll serve --livereload`: levanta el sitio local.
- `bundle exec jekyll build`: compila el sitio en `_site/`.
- `python3 -m venv venv && source venv/bin/activate && pip install gspread pandas oauth2client`: prepara entorno para sincronizar datos.
- `GCP_CREDENTIALS='...' GOOGLE_SHEET_ID='...' python update_sheets.py`: actualiza `_data/*.csv` desde Google Sheets.

Usa cambios pequeños y verificables; evita mezclar contenido, estilo y automatización en un mismo commit.

## Coding Style & Naming Conventions
- Aplicar `.editorconfig`: UTF-8, LF, sin espacios finales, newline final.
- Indentación: 2 espacios (general), 4 espacios en Python.
- Posts con `YYYY-MM-DD-slug.md` o `.markdown`.
- Nombres de includes/layouts en minúsculas y descriptivos (ej.: `_includes/header.html`).
- No reformatear archivos completos si solo cambias una sección.

## Testing Guidelines
No hay suite de tests automatizados; la validación es de build y revisión manual.

- Ejecutar `bundle exec jekyll build` antes de PR.
- Revisar en local con `bundle exec jekyll serve` (navegación, enlaces, paginación, render móvil).
- Si cambias `_data/` o `update_sheets.py`, inspeccionar el diff de CSV y validar columnas esperadas.

## Commit & Pull Request Guidelines
- Commits imperativos y concretos (`Update CSVs from Google Sheets`, `Refactor Google Sheets integration`).
- Un objetivo por commit.
- PR debe incluir:
  - resumen de cambios y motivo,
  - rutas afectadas (`_posts/`, `_data/`, `.github/workflows/`),
  - evidencia visual si hay cambios UI,
  - notas de configuración/secrets si aplica.

## Security & Configuration Tips
- No subir credenciales (`.env`, keys, JSON de service account).
- Mantener secretos en GitHub Actions Secrets (`GCP_CREDENTIALS`, `GOOGLE_SHEET_ID`).
- No añadir scripts de terceros o tracking sin justificación técnica y de privacidad.
