import random
from pyfiglet import Figlet

# Crear el objeto Figlet
figlet = Figlet()

# Obtener la lista de fuentes disponibles
fonts = figlet.getFonts()

# Solicitar al usuario el nombre de una fuente
font_name = input("Ingrese el nombre de una fuente (o presione Enter para seleccionar una aleatoria): ")

# Seleccionar una fuente aleatoria si no se ingresa ninguna
if not font_name:
    font_name = random.choice(fonts)

# Verificar si la fuente ingresada es válida
if font_name not in fonts:
    print(f"La fuente '{font_name}' no es válida. Se seleccionará una fuente aleatoria.")
    font_name = random.choice(fonts)

# Establecer la fuente seleccionada
figlet.setFont(font=font_name)

# Solicitar al usuario un texto
text = input("Ingrese el texto que desea convertir: ")

# Imprimir el texto usando la fuente apropiada
print(figlet.renderText(text))