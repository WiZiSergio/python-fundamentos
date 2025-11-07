"""
Calculadora v6 - Persistencia con JSON (VERSIÓN FINAL)
=======================================================

En esta sexta y última versión añadirás persistencia: el historial se guardará
en un archivo JSON para que no se pierda al cerrar el programa.

Conceptos aplicados:
- Lectura y escritura de archivos
- Módulo json (load, dump)
- Manejo de excepciones (FileNotFoundError, JSONDecodeError)
- Context managers (with open...)
- Persistencia de datos

Instrucciones:
1. Importa el módulo json
2. Crea funciones para cargar y guardar el historial en JSON
3. Carga el historial al iniciar el programa
4. Guarda el historial al salir
5. Añade opción para limpiar el historial
"""

import json
import os


# Nombre del archivo donde se guardará el historial
ARCHIVO_HISTORIAL = "historial_calculadora.json"

# Lista global para el historial
historial = []


# ===== FUNCIONES DE OPERACIONES =====

def sumar(a, b):
    """Suma dos números."""
    return a + b


def restar(a, b):
    """Resta dos números."""
    return a - b


def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b


def dividir(a, b):
    """Divide dos números."""
    return a / b


# ===== FUNCIONES DE INTERFAZ =====

def mostrar_menu():
    """Muestra el menú de opciones de la calculadora."""
    print("\n=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Ver historial")
    print("6. Limpiar historial")  # Nueva opción
    print("7. Salir")  # Ahora es la opción 7


def obtener_numeros():
    """Pide dos números al usuario y los devuelve."""
    num1 = float(input("Primer número: "))
    num2 = float(input("Segundo número: "))
    return num1, num2


# ===== FUNCIONES DE HISTORIAL (memoria) =====

def guardar_operacion(num1, num2, operacion, resultado):
    """Guarda una operación en el historial (en memoria)."""
    operacion_dict = {
        "num1": num1,
        "num2": num2,
        "operacion": operacion,
        "resultado": resultado
    }
    historial.append(operacion_dict)


def mostrar_historial():
    """Muestra todas las operaciones del historial."""
    if not historial:
        print("📭 No hay operaciones en el historial")
        return

    print("\n📜 HISTORIAL DE OPERACIONES:")
    for i, op in enumerate(historial, 1):
        print(f"{i}. {op['num1']} {op['operacion']} {op['num2']} = {op['resultado']:.2f}")


# ===== NUEVAS FUNCIONES DE PERSISTENCIA (archivos JSON) =====

def cargar_historial():
    """Carga el historial desde el archivo JSON.

    Returns:
        Lista con el historial cargado, o lista vacía si no existe el archivo.
    """
    # TODO 2: Intenta cargar el archivo JSON
    # try:
    #     with open(ARCHIVO_HISTORIAL, "r", encoding="utf-8") as archivo:
    #         datos = json.load(archivo)
    #         print(f"✅ Historial cargado: {len(datos)} operaciones")
    #         return datos
    # except FileNotFoundError:
    #     # El archivo no existe (primera vez que se ejecuta)
    #     print("📝 No hay historial previo, iniciando uno nuevo")
    #     return []
    # except json.JSONDecodeError:
    #     # El archivo existe pero está corrupto
    #     print("⚠️  Archivo de historial corrupto, iniciando uno nuevo")
    #     return []

    try:
        with open(ARCHIVO_HISTORIAL, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            print(f"✅ Historial cargado: {len(datos)} operaciones")
            return datos
    except FileNotFoundError:
        # El archivo no existe (primera vez que se ejecuta)
        print("📝 No hay historial previo, iniciando uno nuevo")
        return []
    except json.JSONDecodeError:
        # El archivo existe pero está corrupto
        print("⚠️  Archivo de historial corrupto, iniciando uno nuevo")
        return []


def guardar_historial_archivo():
    """Guarda el historial actual en el archivo JSON."""
    try:
        with open(ARCHIVO_HISTORIAL, "w", encoding="utf-8") as archivo:
            # indent=2 hace que el JSON sea más legible
            # ensure_ascii=False permite emojis y caracteres especiales
            json.dump(historial, archivo, indent=2, ensure_ascii=False)
        print("✅ Historial guardado correctamente")
    except Exception as e:
        print(f"❌ Error al guardar el historial: {e}")


def limpiar_historial():
    """Limpia el historial en memoria y elimina el archivo."""
    global historial
    # Pide confirmación al usuario
    confirmacion = input("⚠️  ¿Estás seguro de que quieres limpiar el historial? (s/n): ")
    if confirmacion.lower() != "s":
        print("❌ Operación cancelada")
        return

    # Vacía la lista en memoria
    historial = []

    # Elimina el archivo si existe
    try:
        if os.path.exists(ARCHIVO_HISTORIAL):
            os.remove(ARCHIVO_HISTORIAL)
        print("🗑️  Historial limpiado correctamente")
    except Exception as e:
        print(f"❌ Error al eliminar el archivo: {e}")


# ===== FUNCIÓN PRINCIPAL =====

def main():
    """Función principal de la calculadora."""
    # Carga el historial al iniciar
    global historial
    print("🔄 Cargando historial...")
    historial = cargar_historial()

    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ").strip()

        # Salir (opción 7)
        if opcion == "7":
            print("💾 Guardando historial...")
            guardar_historial_archivo()
            print("¡Hasta pronto! 👋")
            break

        # Ver historial (opción 5)
        if opcion == "5":
            mostrar_historial()
            continue

        # Limpiar historial (opción 6)
        if opcion == "6":
            limpiar_historial()
            continue

        # Validación de opciones (1-4 son operaciones)
        if opcion not in {"1", "2", "3", "4"}:
            print("❌ Opción no válida")
            continue

        # Obtener números con manejo de errores
        try:
            num1, num2 = obtener_numeros()
        except ValueError:
            print("❌ Entrada inválida. Debes ingresar números.")
            continue

        # Control de división por cero
        if opcion == "4" and num2 == 0:
            print("❌ No se puede dividir por cero")
            continue

        # Ejecutar operación
        if opcion == "1":
            resultado = sumar(num1, num2)
            simbolo = "+"
        elif opcion == "2":
            resultado = restar(num1, num2)
            simbolo = "-"
        elif opcion == "3":
            resultado = multiplicar(num1, num2)
            simbolo = "*"
        else:  # opcion == "4"
            resultado = dividir(num1, num2)
            simbolo = "/"

        print(f"✅ {num1} {simbolo} {num2} = {resultado:.2f}")
        guardar_operacion(num1, num2, simbolo, resultado)


if __name__ == "__main__":
    main()


# ¡FELICIDADES! Has completado toda la serie "La Calculadora que Crece"
#
# 🎉 Lo que has logrado:
# ✅ v1: Suma básica (input, print, variables)
# ✅ v2: 4 operaciones (operadores, if/elif, f-strings)
# ✅ v3: Menú interactivo (while, break/continue, validación)
# ✅ v4: Código modular (funciones, docstrings, return)
# ✅ v5: Historial en memoria (listas, diccionarios, append)
# ✅ v6: Persistencia con JSON (archivos, json.load/dump, excepciones)
#
# Pruebas finales:
# 1. Ejecuta el programa y realiza varias operaciones
# 2. Sal del programa (opción 7)
# 3. Verifica que se creó el archivo "historial_calculadora.json"
# 4. Ábrelo con un editor de texto y verás el JSON con tus operaciones
# 5. Vuelve a ejecutar el programa → el historial debe cargarse automáticamente
# 6. Prueba "Limpiar historial" → el archivo debe desaparecer
#
# 💡 Extensiones opcionales si quieres seguir aprendiendo:
# - Añadir más operaciones (potencia, raíz cuadrada, módulo)
# - Exportar historial a CSV para Excel
# - Interfaz gráfica con Tkinter
# - Tests unitarios con pytest
# - Separar en múltiples módulos (ver carpeta calculadora_modular/)
#
# ¡Has terminado un proyecto completo desde cero hasta una aplicación funcional!
# Este es el tipo de evolución que verás en proyectos reales.
