"""Parser de logs simple

Lee un archivo de logs y genera estadísticas por tipo de evento o fecha.
Formato esperado de log: FECHA HORA TIPO MENSAJE
Ejemplo: 2025-11-07 10:15:30 INFO Sistema iniciado
"""

from collections import defaultdict
from datetime import datetime
import re
from typing import Dict, List, Tuple

class ParserLogs:
    def __init__(self, archivo_entrada: str, archivo_salida: str = "resumen.txt"):
        self.archivo_entrada = archivo_entrada
        self.archivo_salida = archivo_salida
        self.logs_por_tipo: Dict[str, int] = defaultdict(int)
        self.logs_por_fecha: Dict[str, int] = defaultdict(int)
    
    def procesar_linea(self, linea: str) -> Tuple[str, str]:
        """Procesa una línea de log y extrae fecha y tipo"""
        partes = linea.split()
        if len(partes) >= 4:  # Aseguramos que hay suficientes partes
            fecha = partes[0]
            tipo = partes[2]
            return fecha, tipo
        return None, None
    
    def analizar_logs(self):
        """Lee y analiza el archivo de logs"""
        try:
            with open(self.archivo_entrada, 'r', encoding='utf-8') as f:
                for linea in f:
                    fecha, tipo = self.procesar_linea(linea.strip())
                    if fecha and tipo:
                        self.logs_por_fecha[fecha] += 1
                        self.logs_por_tipo[tipo] += 1
            return True
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo {self.archivo_entrada}")
            return False
    
    def generar_resumen(self):
        """Genera el resumen de los logs"""
        if not self.logs_por_tipo or not self.logs_por_fecha:
            return "No hay datos para generar el resumen"
        
        resumen = []
        resumen.append("=== RESUMEN DE LOGS ===\n")
        
        # Resumen por tipo
        resumen.append("EVENTOS POR TIPO:")
        for tipo, cantidad in sorted(self.logs_por_tipo.items()):
            resumen.append(f"{tipo}: {cantidad}")
        
        resumen.append("\nEVENTOS POR FECHA:")
        for fecha, cantidad in sorted(self.logs_por_fecha.items()):
            resumen.append(f"{fecha}: {cantidad}")
        
        # Estadísticas generales
        total_eventos = sum(self.logs_por_tipo.values())
        resumen.append(f"\nTotal de eventos: {total_eventos}")
        resumen.append(f"Días diferentes: {len(self.logs_por_fecha)}")
        if self.logs_por_fecha:
            promedio = total_eventos / len(self.logs_por_fecha)
            resumen.append(f"Promedio de eventos por día: {promedio:.2f}")
        
        return "\n".join(resumen)
    
    def guardar_resumen(self):
        """Guarda el resumen en un archivo"""
        resumen = self.generar_resumen()
        try:
            with open(self.archivo_salida, 'w', encoding='utf-8') as f:
                f.write(resumen)
            print(f"Resumen guardado en {self.archivo_salida}")
            return True
        except Exception as e:
            print(f"Error al guardar el resumen: {e}")
            return False

def main():
    # Archivo de ejemplo (si no existe, crear uno)
    ejemplo_logs = [
        "2025-11-07 10:15:30 INFO Sistema iniciado",
        "2025-11-07 10:16:45 WARNING Espacio en disco bajo",
        "2025-11-07 11:20:15 ERROR Base de datos no responde",
        "2025-11-08 09:00:00 INFO Respaldo iniciado",
        "2025-11-08 09:30:00 INFO Respaldo completado",
        "2025-11-08 15:45:30 WARNING Memoria baja",
    ]
    
    # Crear archivo de logs de ejemplo
    with open("ejemplo.log", 'w', encoding='utf-8') as f:
        for log in ejemplo_logs:
            f.write(log + "\n")
    
    # Procesar logs
    parser = ParserLogs("ejemplo.log")
    if parser.analizar_logs():
        parser.guardar_resumen()
        # Mostrar resumen en pantalla también
        print("\n" + parser.generar_resumen())

if __name__ == "__main__":
    main()