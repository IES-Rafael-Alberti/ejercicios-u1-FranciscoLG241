def main():
    
    nombre = input("Introduce tu nombre: ")
    edad = int(input("Introduce tu edad: "))
    
    if not nombre:
        nombre = "Desconocido"
    while (0 > edad or edad >125):
        print("No es posible")
        edad = int(input("Introduce tu edad: "))
    edad_2 = 125 - edad
    print(f"Te llamas {nombre} y tienes {edad} años, te quedan {edad_2} años por cumplir")
             
if __name__ == "__main__":
    main()        
    