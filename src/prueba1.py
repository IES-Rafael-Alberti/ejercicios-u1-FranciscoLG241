def primer_numero():
    num1 = int(input("Introduce un primer número: "))
    return num1

def segundo_numero():
    num2 = int(input("Introduce un primer número: "))
    return num2

def comparador(num1: str,num2: str) -> int:
    if num1 == num2:
        return 0
    elif num1 > num2:
        return num1
    else:
        return num2
    

def main():
    num1 = primer_numero()
    num2 = segundo_numero()
    
    if num1 > num2:
        comparador(num1, num2)
    
    elif num1 < num2:
        comparador(num1, num2)
        
    else:
        comparador(num1, num2)
    

if __name__ == "__main__":
    main()