def saludo(nom):
    return "Hola, " + nom + "."

def main():
    nombre = input("Introduce nombre: ")
    print(saludo(nombre))
    
    if __name__== "__main__":
        main()


nombre = input("Escribe tu nombre: ")
print (f"Hola, {nombre}")
