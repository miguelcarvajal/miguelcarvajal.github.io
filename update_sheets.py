
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import os

# Autenticación con la API de Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_dict(json.loads(os.environ["GCP_CREDENTIALS"]), scope)
client = gspread.authorize(credentials)

# ID de tu Google Sheet
spreadsheet_id = "15sKk88cRmRlp3OWAeBYRwx31pCXjqpR60yeqlBFAduI"
spreadsheet = client.open_by_key(spreadsheet_id)

# Lista de nombres de las hojas
sheet_names = ["articulos", "art_no_index", "libros", "capitulos", "proyectos", "congresos", "peer_review", "comites", "seminarios", "prensa", "docencia", "metricas"]

# Carpeta donde se guardarán los CSVs
output_folder = "_data"

# Crear la carpeta si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Descargar cada hoja como CSV
for sheet_name in sheet_names:
    print(f"Processing sheet: {sheet_name}")
    sheet = spreadsheet.worksheet(sheet_name)
    
    # Obtener todas las filas y cabeceras
    rows = sheet.get_all_values()
    headers = rows[0]
    
    # Verificar si las cabeceras son únicas
    if len(headers) != len(set(headers)):
        # Si no son únicas, hacer las cabeceras únicas
        unique_headers = []
        header_counts = {}
        for header in headers:
            if header in header_counts:
                header_counts[header] += 1
                new_header = f"{header}_{header_counts[header]}"
            else:
                header_counts[header] = 0
                new_header = header
            unique_headers.append(new_header)
        headers = unique_headers
    
    # Convertir a DataFrame
    df = pd.DataFrame(rows[1:], columns=headers)
    
    # Guardar como CSV
    csv_path = os.path.join(output_folder, f"{sheet_name}.csv")
    print(f"Saving to {csv_path}")
    df.to_csv(csv_path, index=False)

