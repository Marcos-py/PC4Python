import requests
import sqlite3
from pymongo import MongoClient
from datetime import datetime, timedelta

# Configuración de la API de SUNAT
url_base = "https://api.apis.net.pe/v1/tipo-cambio-sunat"

# Configuración de la base de datos SQLite
conn_sqlite = sqlite3.connect('base.db')
cursor_sqlite = conn_sqlite.cursor()

# Configuración de la base de datos MongoDB
client_mongo = MongoClient('localhost', 27017)  # Reemplaza con tu configuración de MongoDB
db_mongo = client_mongo['sunat']
coleccion_mongo = db_mongo['tipo_cambio']

# Crear la tabla en SQLite si no existe
cursor_sqlite.execute('''
    CREATE TABLE IF NOT EXISTS sunat_info (
        fecha TEXT PRIMARY KEY,
        compra REAL,
        venta REAL
    )
''')

# Obtener datos del año 2023
fecha_inicio = datetime(2023, 1, 1)
fecha_fin = datetime(2023, 12, 31)

fecha_actual = fecha_inicio
while fecha_actual <= fecha_fin:
    fecha_str = fecha_actual.strftime("%Y-%m-%d")
    url = f"{url_base}?fecha={fecha_str}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Verificar si hubo errores en la solicitud

        data = response.json()

        # Insertar datos en SQLite
        cursor_sqlite.execute('''
            INSERT OR REPLACE INTO sunat_info (fecha, compra, venta)
            VALUES (?, ?, ?)
        ''', (fecha_str, data.get('compra'), data.get('venta')))
        conn_sqlite.commit()

        # Insertar datos en MongoDB
        documento = {
            'fecha': fecha_str,
            'compra': data.get('compra'),
            'venta': data.get('venta')
        }
        coleccion_mongo.insert_one(documento)

        print(f"Datos para {fecha_str} insertados en las bases de datos.")

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos para {fecha_str}: {e}")

    fecha_actual += timedelta(days=1)

# Mostrar contenido de la tabla SQLite
cursor_sqlite.execute("SELECT * FROM sunat_info")
rows = cursor_sqlite.fetchall()
for row in rows:
    print(row)

# Cerrar conexiones
conn_sqlite.close()
client_mongo.close()