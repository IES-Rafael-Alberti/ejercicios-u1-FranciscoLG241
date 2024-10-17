def main():

    num1 = int(input("Introduce un primer número: "))
    num2 = int(input("Introduce un segundo número: "))
    if (num1 == num2):
        print("Los números no pueden ser iguales")
    else:    
        if (num1 > num2):
            num3 = num1 - num2
            print(f"El número menor es el {num2} y entre ellos existen {num3} números enteros")
        else:
            num3 = num2 - num1
            print(f"El número menor es el {num1} y entre ellos existen {num3} números enteros")
    

if __name__ == "__main__":
    main()