
def solicitar_horas():
    horas = int(input("Horas de trabajo: "))
    return horas

def solicitar_coste():
    coste = int(input("Coste por hora: "))
    return coste

def operacion_trabajo(horas, coste):
    importe = horas * coste
    return importe

def main():
    horas = solicitar_horas()
    coste = solicitar_coste()
    total = operacion_trabajo(horas, coste)
    print(f"El importe total es: {total}")
    
if __name__ == "__main__":
    main()


   
    
    