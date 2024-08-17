import requests
import zipfile

# Descargar la imagen
url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
response = requests.get(url)

with open("imagen.jpg", "wb") as f:
    f.write(response.content)

# Comprimir la imagen en un archivo zip
with zipfile.ZipFile("imagen.zip", "w") as zip_file:
    zip_file.write("imagen.jpg")

# Descomprimir el archivo zip
with zipfile.ZipFile("imagen.zip", "r") as zip_file:
    zip_file.extractall()