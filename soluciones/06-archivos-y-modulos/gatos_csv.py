"""Ejercicio autónomo 1: Resumen de gatos en CSV

Guarda información de gatos en un archivo CSV
"""

# Lista de gatos de ejemplo
gatos = [
    ["Nombre", "Edad", "Color"],
    ["Luna", "3", "gris"],
    ["Simba", "2", "naranja"],
    ["Michi", "5", "blanco y negro"],
    ["Neko", "1", "negro"]
]

# Guardar en archivo CSV
print("Guardando información de gatos en gatos.csv...")
try:
    with open("gatos.csv", "w", encoding="utf-8") as archivo:
        for gato in gatos:
            linea = ",".join(gato) + "\n"
            archivo.write(linea)
    print("Archivo gatos.csv creado correctamente.")
except Exception as e:
    print(f"Error al guardar el archivo: {e}")

# Leer y mostrar el contenido
print("\nContenido del archivo gatos.csv:")
try:
    with open("gatos.csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            print(linea.strip())
except FileNotFoundError:
    print("Error: No se encontró el archivo gatos.csv")