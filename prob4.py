import requests

# Descargar el archivo de temperaturas
url = "https://github.com/gdelgador/ProgramacionPython202407/blob/main/Modulo4/src/temperaturas.txt?raw=true"
response = requests.get(url)

# Guardar el archivo localmente
with open("temperaturas.txt", "wb") as f:
    f.write(response.content)

# Inicializar variables para almacenar las temperaturas
temperaturas = []

# Leer el archivo y procesar las temperaturas
with open("temperaturas.txt", "r") as f:
    for linea in f:
        fecha, temperatura = linea.strip().split(",")
        try:
            temperaturas.append(float(temperatura))
        except ValueError:
            print(f"Error al procesar la temperatura en la línea: {linea.strip()}")

# Calcular la temperatura promedio, máxima y mínima
if temperaturas:
    temperatura_promedio = sum(temperaturas) / len(temperaturas)
    temperatura_maxima = max(temperaturas)
    temperatura_minima = min(temperaturas)

    # Escribir los resultados en el archivo resumen_temperaturas.txt
    with open("resumen_temperaturas.txt", "w") as f:
        f.write(f"Temperatura promedio: {temperatura_promedio:.2f}\n")
        f.write(f"Temperatura máxima: {temperatura_maxima:.2f}\n")
        f.write(f"Temperatura mínima: {temperatura_minima:.2f}\n")

    print("Resumen de temperaturas guardado en 'resumen_temperaturas.txt'")
else:
    print("No se encontraron temperaturas válidas en el archivo.")