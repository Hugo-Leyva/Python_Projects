# Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje "es vocal".
# Se debe validar que el usuario ingrese solo un caracter. Si ingresa un string de mas de un caracter,
# informarle que no se puede procesar el dato.
vocal = ["a","e","i","o","u","A","E","I","O","U"]
letra = input(f'Ingresa una letra: ')
if len(letra)!=1:
    print("Debe ser sólo una letra")
elif letra in vocal:
    print("Es vocal")
if letra != vocal:
    print("No es Vocal")