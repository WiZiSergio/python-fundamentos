"""Guiado 1: Clasificador simple

Pide un número y lo clasifica como negativo, cero o positivo.
Valida ValueError para entrada no numérica.
"""

try:
    texto = input("Ingresa un número: ")
    numero = float(texto)
    
    if numero < 0:
        print("Negativo")
    elif numero == 0:
        print("Cero")
    else:
        print("Positivo")
except ValueError:
    print("Entrada inválida")