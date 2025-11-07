"""Estadísticas del refugio de gatos

Calcula estadísticas básicas sobre los gatos del refugio:
- Conteo total
- Media de peso y edad
- Mediana de peso y edad
- Top-3 gatos más pesados
"""

import statistics
from typing import List, Tuple, Optional
import json

class RefugioStats:
    def __init__(self, gatos: List[Tuple[float, int]]):
        """
        Inicializa con lista de tuplas (peso, edad)
        """
        self.gatos = gatos
        self.pesos = [peso for peso, _ in gatos]
        self.edades = [edad for _, edad in gatos]
    
    def calcular_estadisticas(self) -> dict:
        """Calcula todas las estadísticas básicas"""
        stats = {
            "total_gatos": len(self.gatos),
            "peso": {
                "media": statistics.mean(self.pesos),
                "mediana": statistics.median(self.pesos)
            },
            "edad": {
                "media": statistics.mean(self.edades),
                "mediana": statistics.median(self.edades)
            },
            "top_pesados": sorted(self.gatos, reverse=True)[:3]
        }
        return stats
    
    def mostrar_resumen(self, stats: dict):
        """Muestra el resumen por pantalla"""
        print("\n=== Estadísticas del Refugio ===")
        print(f"Total de gatos: {stats['total_gatos']}")
        
        print("\nEstadísticas de peso:")
        print(f"- Media: {stats['peso']['media']:.2f} kg")
        print(f"- Mediana: {stats['peso']['mediana']:.2f} kg")
        
        print("\nEstadísticas de edad:")
        print(f"- Media: {stats['edad']['media']:.1f} años")
        print(f"- Mediana: {stats['edad']['mediana']:.1f} años")
        
        print("\nTop 3 gatos más pesados:")
        for i, (peso, edad) in enumerate(stats['top_pesados'], 1):
            print(f"{i}. {peso:.2f} kg ({edad} años)")
    
    def guardar_resumen(self, stats: dict, archivo: str):
        """Guarda el resumen en un archivo JSON"""
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(stats, f, indent=2)
        print(f"\nResumen guardado en {archivo}")

def main():
    # Datos de ejemplo (peso en kg, edad en años)
    gatos_ejemplo = [
        (4.5, 3),  # 4.5 kg, 3 años
        (3.8, 2),
        (5.2, 5),
        (4.0, 1),
        (6.1, 4),
        (3.5, 2),
        (4.8, 6),
        (5.5, 3)
    ]
    
    # Crear instancia y calcular estadísticas
    refugio = RefugioStats(gatos_ejemplo)
    stats = refugio.calcular_estadisticas()
    
    # Mostrar resultados
    refugio.mostrar_resumen(stats)
    
    # Guardar en archivo
    refugio.guardar_resumen(stats, "estadisticas_refugio.json")

if __name__ == "__main__":
    main()