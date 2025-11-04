"""Autónomo 2: Contador de letras

Cuenta letras en un string usando un bucle.
"""

texto = input("Ingresa un texto: ")
contador = 0

for caracter in texto:
    if caracter.isalpha():
        contador += 1

print(f"Total de letras: {contador}")