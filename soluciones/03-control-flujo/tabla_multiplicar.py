"""Autónomo 3: Tabla de multiplicar

Genera una tabla de multiplicar del 1 al 5 usando for anidados.
"""

print("Tablas de multiplicar del 1 al 5:")
print("-" * 40)

for i in range(1, 6):
    print(f"\nTabla del {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
