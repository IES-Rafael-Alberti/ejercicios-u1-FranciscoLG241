
def solicitar_nombre():
    nombre = input("Escribe tu nombre: ")
    return f"Hola, {nombre}"

def solicitar_nombre_test(nombre):
    return nombre

def main():
    nombre = solicitar_nombre()
    print (f"{nombre}")

if __name__ == "__main__":
    main()
