def suma_entero(n):
    suma = (n * (n + 1)) // 2
    return suma

def main():
    n = input("Introduce un entero positivo: ")
    if n.isdigit():
            n = int(n)
            resultado = suma_entero(n)
            print(f"La suma de los enteros desde 1 hasta {n} es: {resultado}")
    else:
            print("Por favor, introduce un número entero válido.")
            
if __name__ == "__main__":
    main()
        