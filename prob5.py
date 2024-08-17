import os

def guardar_tabla(n):
    with open(f"tabla-{n}.txt", "w") as file:
        for i in range(1, 11):
            file.write(f"{n} x {i} = {n * i}\n")
    print(f"Tabla de multiplicar del {n} guardada en tabla-{n}.txt")

def leer_tabla(n):
    try:
        with open(f"tabla-{n}.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"El fichero tabla-{n}.txt no existe.")

def leer_linea_tabla(n, m):
    try:
        with open(f"tabla-{n}.txt", "r") as file:
            lines = file.readlines()
            if 1 <= m <= 10:
                print(lines[m-1].strip())
            else:
                print("El número m debe estar entre 1 y 10.")
    except FileNotFoundError:
        print(f"El fichero tabla-{n}.txt no existe.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Guardar tabla de multiplicar")
        print("2. Leer tabla de multiplicar")
        print("3. Leer línea específica de la tabla de multiplicar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                guardar_tabla(n)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == "2":
            n = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= n <= 10:
                leer_tabla(n)
            else:
                print("El número debe estar entre 1 y 10.")
        elif opcion == "3":
            n = int(input("Ingrese el primer número entero entre 1 y 10: "))
            m = int(input("Ingrese el segundo número entero entre 1 y 10: "))
            if 1 <= n <= 10 and 1 <= m <= 10:
                leer_linea_tabla(n, m)
            else:
                print("Ambos números deben estar entre 1 y 10.")
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

if __name__ == "__main__":
    menu()