"""Ejercicio guiado 1 y 2: Escribir y leer archivo

Crea escribir.txt con tres líneas y luego léelo imprimiendo
las líneas numeradas.
"""

# Parte 1: Escribir archivo
print("Escribiendo archivo...")
with open("escribir.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Primera línea\n")
    archivo.write("Segunda línea\n")
    archivo.write("Tercera línea\n")

print("Archivo creado correctamente.")

# Parte 2: Leer archivo
print("\nLeyendo archivo:")
try:
    with open("escribir.txt", "r", encoding="utf-8") as archivo:
        for i, linea in enumerate(archivo, 1):
            print(f"{i}: {linea.strip()}")
except FileNotFoundError:
    print("Error: No se encontró el archivo escribir.txt")