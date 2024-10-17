def main():
    num1 = int(input("Introduce un primer número: "))
    incremento = int(input("Introduce un incremento : "))
    total = int(input("Introduce el total de la serie: "))
    
    while total < 0 or incremento < 0:
        print("**ERROR**")
        incremento = int(input("Introduce un incremento : "))
        total = int(input("Introduce el total de la serie: "))
    
    serie = ""
    
    for i in range(total):
        serie += str(num1 + i)
        if i < total - 1:
            serie += "-"
    
    print(f"SERIE => {serie}")

if __name__ == "__main__":
    main()
