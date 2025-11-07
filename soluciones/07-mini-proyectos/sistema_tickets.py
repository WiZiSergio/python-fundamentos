"""Sistema de tickets simple

Implementa un sistema básico de tickets con las siguientes operaciones:
- Crear ticket
- Listar tickets
- Cerrar ticket
- Guardar/Cargar tickets
"""

import json
from typing import Dict, List
from datetime import datetime

class SistemaTickets:
    def __init__(self, archivo: str = "tickets.json"):
        self.tickets: Dict[int, dict] = {}
        self.siguiente_id = 1
        self.archivo = archivo
        self.cargar_tickets()
    
    def crear_ticket(self, titulo: str, descripcion: str) -> int:
        """Crea un nuevo ticket y retorna su ID"""
        ticket = {
            "id": self.siguiente_id,
            "titulo": titulo,
            "descripcion": descripcion,
            "estado": "abierto",
            "fecha_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "fecha_cierre": None
        }
        
        self.tickets[self.siguiente_id] = ticket
        self.siguiente_id += 1
        self.guardar_tickets()
        return ticket["id"]
    
    def listar_tickets(self, solo_abiertos: bool = False) -> List[dict]:
        """Lista todos los tickets o solo los abiertos"""
        tickets = self.tickets.values()
        if solo_abiertos:
            tickets = [t for t in tickets if t["estado"] == "abierto"]
        return list(tickets)
    
    def cerrar_ticket(self, ticket_id: int) -> bool:
        """Cierra un ticket por su ID"""
        if ticket_id not in self.tickets:
            return False
        
        if self.tickets[ticket_id]["estado"] == "cerrado":
            return False
        
        self.tickets[ticket_id]["estado"] = "cerrado"
        self.tickets[ticket_id]["fecha_cierre"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.guardar_tickets()
        return True
    
    def guardar_tickets(self):
        """Guarda los tickets en un archivo JSON"""
        with open(self.archivo, 'w', encoding='utf-8') as f:
            json.dump({"tickets": self.tickets, "siguiente_id": self.siguiente_id}, f, indent=2)
    
    def cargar_tickets(self):
        """Carga los tickets desde el archivo JSON"""
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.tickets = data["tickets"]
                self.siguiente_id = data["siguiente_id"]
        except FileNotFoundError:
            self.tickets = {}
            self.siguiente_id = 1

def mostrar_menu():
    print("\n=== Sistema de Tickets ===")
    print("1. Crear ticket")
    print("2. Listar tickets")
    print("3. Cerrar ticket")
    print("4. Salir")
    return input("Seleccione una opción: ")

def main():
    sistema = SistemaTickets()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            titulo = input("Título del ticket: ")
            descripcion = input("Descripción: ")
            ticket_id = sistema.crear_ticket(titulo, descripcion)
            print(f"Ticket creado con ID: {ticket_id}")
        
        elif opcion == "2":
            solo_abiertos = input("¿Mostrar solo tickets abiertos? (s/n): ").lower() == 's'
            tickets = sistema.listar_tickets(solo_abiertos)
            print("\n=== Lista de Tickets ===")
            for t in tickets:
                print(f"ID: {t['id']} - {t['titulo']} ({t['estado']})")
                print(f"Creado: {t['fecha_creacion']}")
                if t['fecha_cierre']:
                    print(f"Cerrado: {t['fecha_cierre']}")
                print(f"Descripción: {t['descripcion']}\n")
        
        elif opcion == "3":
            try:
                ticket_id = int(input("ID del ticket a cerrar: "))
                if sistema.cerrar_ticket(ticket_id):
                    print("Ticket cerrado correctamente")
                else:
                    print("No se pudo cerrar el ticket")
            except ValueError:
                print("ID inválido")
        
        elif opcion == "4":
            break
        
        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()