def suma_entero(n):
    suma = (n * (n + 1)) // 2
    return f"La suma de los enteros desde 1 hasta {n} es: {suma}"

def main():
    n = input("Introduce un entero positivo: ")
    if n.isdigit():
            n = int(n)
            resultado = suma_entero(n)
            print(resultado)
    else:
            print("Por favor, introduce un número entero válido.")
            
if __name__ == "__main__":
    main()
        