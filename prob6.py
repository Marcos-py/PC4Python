def contar_lineas_codigo(ruta_archivo):
    """
    Cuenta las líneas de código de un archivo .py, excluyendo comentarios y líneas en blanco.

    Args:
        ruta_archivo: La ruta completa al archivo .py.

    Returns:
        El número de líneas de código, o None si la ruta es inválida o el archivo no termina en .py.
    """
    if not ruta_archivo.endswith(".py"):
        return None

    try:
        with open(ruta_archivo, "r") as f:
            lineas = f.readlines()  # Leer todas las líneas del archivo
            lineas_codigo = 0
            for linea in lineas:
                linea = linea.strip()  # Eliminar espacios en blanco al principio y al final
                if linea and not linea.startswith("#"):  # Contar solo líneas no vacías y sin comentarios
                    lineas_codigo += 1
        return lineas_codigo
    except FileNotFoundError:
        return None

# Solicitar la ruta del archivo al usuario
ruta_archivo = input("Ingrese la ruta del archivo .py: ")

# Contar las líneas de código y mostrar el resultado
resultado = contar_lineas_codigo(ruta_archivo)
if resultado is not None:
    print(f"El archivo {ruta_archivo} tiene {resultado} líneas de código.")
else:
    print("Ruta inválida o archivo no es un archivo .py.")