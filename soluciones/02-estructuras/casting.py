texto = input("Ingresa un número entero: ")
try:
    valor = int(texto)
    print(f"Ingresaste el entero: {valor}")
except ValueError:
    print("Entrada inválida")
