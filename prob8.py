import csv
import sqlite3
# from pymongo import MongoClient  # Si prefieres usar MongoDB

# Conexión a la base de datos SQLite
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

# # Conexión a MongoDB
# client = MongoClient('localhost', 27017)
# db = client['sunat']
# coleccion = db['tipo_cambio']

# Leer el archivo de ventas
with open('ventas.csv', 'r') as archivo_ventas:
    lector_csv = csv.reader(archivo_ventas)
    next(lector_csv)  # Saltar la primera línea (encabezados)

    total_dolares = 0
    total_soles = 0

    for fila in lector_csv:
        producto, fecha, precio_dolares = fila
        precio_dolares = float(precio_dolares)

        # Obtener el tipo de cambio de la base de datos SQLite
        cursor.execute("SELECT venta FROM sunat_info WHERE fecha=?", (fecha,))
        resultado = cursor.fetchone()
        if resultado:
            tipo_cambio = resultado[0]
            precio_soles = precio_dolares * tipo_cambio
            total_dolares += precio_dolares
            total_soles += precio_soles

            print(f"{producto}: ${precio_dolares:.2f} (USD) - S/.{precio_soles:.2f} (PEN)")
        else:
            print(f"No se encontró tipo de cambio para la fecha {fecha}.")

    print(f"\nTotal en dólares: ${total_dolares:.2f}")
    print(f"Total en soles: S/.{total_soles:.2f}")

# Cerrar conexiones
conn.close()
# client.close()  # Si usaste MongoDB