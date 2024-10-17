def comprobar_numeros(cadena: str) -> bool:
    if cadena.startswith("-"):
        cadena = cadena
    return cadena.isdigit()

def introducir_numero(msj: str) -> int:
    valor = input(msj).strip()
    
    if comprobar_numeros(valor) == True:
        return int(valor)
    elif valor.lower() == "fin":
        return -1
    else:
        return -2

def main():
    
    cantidad = 0
    suma = 0
    media = 0
    salir = False
    
    while not salir:
        num = introducir_numero("Introducir un número: ")
        
        if num == -1:
            #fin
            salir = True
        elif num == -2:
            print("Entrada inválida")
        else:
            cantidad += 1
            suma += num
            
    if cantidad != 0:
        media = suma / cantidad                
        