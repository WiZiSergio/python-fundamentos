"""Script que usa el módulo utiles.py

Ejemplo de uso de las funciones leer_lineas y guardar_lineas.
"""

import os
from utiles import leer_lineas, guardar_lineas

def main():
    # Pedir ruta de archivo al usuario
    ruta = input("Ingresa la ruta del archivo a leer: ")
    
    # Validar si el archivo existe
    if not os.path.exists(ruta):
        print(f"Error: El archivo {ruta} no existe")
        return
    
    try:
        # Leer líneas del archivo
        print(f"\nLeyendo archivo {ruta}:")
        lineas = leer_lineas(ruta)
        for i, linea in enumerate(lineas, 1):
            print(f"{i}: {linea}")
        
        # Guardar una copia del archivo con líneas numeradas
        ruta_salida = "salida.txt"
        lineas_numeradas = [f"Línea {i}: {linea}" for i, linea in enumerate(lineas, 1)]
        guardar_lineas(ruta_salida, lineas_numeradas)
        print(f"\nSe ha guardado una copia numerada en {ruta_salida}")
        
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo {ruta}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()