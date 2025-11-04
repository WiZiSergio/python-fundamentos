"""Guiado 2: Suma acumulada

Suma números introducidos por el usuario hasta que escriba 'fin'.
"""

total = 0.0
while True:
    entrada = input("Ingresa un número (o 'fin' para terminar): ").strip()
    if entrada.lower() == "fin":
        break
    try:
        valor = float(entrada)
        total += valor
    except ValueError:
        print("Entrada inválida, intenta de nuevo.")
        continue

print(f"Total: {total}")