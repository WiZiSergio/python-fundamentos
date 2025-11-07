"""Desafío: Bigotes Felices (logs)

Analiza un archivo de logs y cuenta las visitas por día.
"""

from collections import defaultdict
import re
from datetime import datetime

def analizar_logs(ruta_entrada, ruta_salida):
    """
    Analiza un archivo de logs y genera un resumen de visitas por día.
    
    Args:
        ruta_entrada (str): Ruta del archivo de logs
        ruta_salida (str): Ruta donde guardar el resumen
    """
    # Diccionario para contar visitas por día
    visitas_por_dia = defaultdict(int)
    
    try:
        # Leer y procesar el archivo de logs
        with open(ruta_entrada, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                # Buscar la fecha en el formato YYYY-MM-DD
                match = re.search(r'\d{4}-\d{2}-\d{2}', linea)
                if match:
                    fecha = match.group()
                    visitas_por_dia[fecha] += 1
        
        # Ordenar las fechas
        fechas_ordenadas = sorted(visitas_por_dia.keys())
        
        # Guardar el resumen
        with open(ruta_salida, "w", encoding="utf-8") as archivo:
            archivo.write("Fecha,Visitas\n")
            for fecha in fechas_ordenadas:
                archivo.write(f"{fecha},{visitas_por_dia[fecha]}\n")
                
        print(f"Resumen guardado en {ruta_salida}")
        
        # Mostrar estadísticas
        total_visitas = sum(visitas_por_dia.values())
        print(f"\nEstadísticas:")
        print(f"Total de días: {len(visitas_por_dia)}")
        print(f"Total de visitas: {total_visitas}")
        if visitas_por_dia:
            promedio = total_visitas / len(visitas_por_dia)
            print(f"Promedio de visitas por día: {promedio:.2f}")
            
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {ruta_entrada}")
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")

if __name__ == "__main__":
    # Archivos de entrada y salida
    archivo_logs = "visitas.log"
    archivo_resumen = "resumen_visitas.csv"
    
    # Procesar logs
    print(f"Analizando archivo de logs {archivo_logs}...")
    analizar_logs(archivo_logs, archivo_resumen)