"""Solución - Guiado 2: Casting y validación

Pide un número por input y convierte a int dentro de try/except.
Si falla, muestra 'Entrada inválida'.
"""

texto = input("Ingresa un número entero: ")
try:
    valor = int(texto)
    print(f"Ingresaste el entero: {valor}")
except ValueError:
    print("Entrada inválida")
