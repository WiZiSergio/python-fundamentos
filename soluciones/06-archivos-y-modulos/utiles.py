"""Módulo de utilidades para manejo de archivos

Proporciona funciones para leer y guardar líneas en archivos.
"""

def leer_lineas(ruta):
    """
    Lee las líneas de un archivo y las devuelve como lista.
    
    Args:
        ruta (str): Ruta al archivo a leer
        
    Returns:
        list: Lista de líneas del archivo
        
    Raises:
        FileNotFoundError: Si el archivo no existe
    """
    with open(ruta, "r", encoding="utf-8") as archivo:
        return [linea.strip() for linea in archivo]

def guardar_lineas(ruta, lineas):
    """
    Guarda una lista de líneas en un archivo.
    
    Args:
        ruta (str): Ruta donde guardar el archivo
        lineas (list): Lista de líneas a guardar
        
    Raises:
        Exception: Si hay un error al escribir el archivo
    """
    with open(ruta, "w", encoding="utf-8") as archivo:
        for linea in lineas:
            archivo.write(str(linea) + "\n")