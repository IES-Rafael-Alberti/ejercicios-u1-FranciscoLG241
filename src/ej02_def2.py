
def operacion_horas(horas, coste):
    importe = horas * coste
    return importe

def main():
    horas = float(input("Introduce el número de horas: "))
    coste = float(input("Introduce el coste por hora: "))
    print(f"El importe total es de {operacion_horas(horas, coste)}")

if __name__ == "__main__":
    main()



   
    
    