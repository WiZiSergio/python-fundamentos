"""Autónomo 4: Verificador de contraseñas

Pide al usuario que ingrese una contraseña hasta que cumpla con los criterios:
- Al menos 8 caracteres
- Al menos una letra mayúscula
- Al menos un número
"""

def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres"
    
    tiene_mayuscula = False
    tiene_numero = False
    
    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
        if caracter.isdigit():
            tiene_numero = True
            
    if not tiene_mayuscula:
        return False, "La contraseña debe tener al menos una letra mayúscula"
    if not tiene_numero:
        return False, "La contraseña debe tener al menos un número"
        
    return True, "Contraseña válida"

while True:
    contrasena = input("Ingresa una contraseña: ")
    valida, mensaje = validar_contrasena(contrasena)
    print(mensaje)
    
    if valida:
        break