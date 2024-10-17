def calcular_precio_final(importe_sin_iva: float, tipo_iva: float) -> float:

    if tipo_iva < 0 or tipo_iva > 100:
        tipo_iva = 21  
    iva = (tipo_iva / 100) * importe_sin_iva
    precio_final = importe_sin_iva + iva
    return round(precio_final, 2) 

def main():
    importe_sin_iva = float(input("Introduce el importe sin IVA del artículo: "))
    tipo_iva = float(input("Introduce el tipo de IVA a aplicar (en porcentaje): "))
    
    precio_final = calcular_precio_final(importe_sin_iva, tipo_iva)
    print(f"El precio final del artículo con IVA ({tipo_iva:.2f}) es {precio_final:.2f}€.")

if __name__ == "__main__":
    main()




