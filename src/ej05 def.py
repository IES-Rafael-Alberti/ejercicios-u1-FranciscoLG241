def introduce_el_importe():
    importe_sin_iva = float(input("Introduce el importe sin IVA del artículo: "))
    return importe_sin_iva

def tipo_iva():
    tipo_iva = float(input("Introduce el tipo de IVA a aplicar (en porcentaje): "))
    return tipo_iva

def operacion(importe_sin_iva, tipo_iva):
    iva = (tipo_iva / 100) * importe_sin_iva
    return iva

def final(importe_sin_iva, iva):
    precio_final = importe_sin_iva + iva
    print(f"El precio final del artículo es: {precio_final:.2f}€")

def main():
    importe = introduce_el_importe()
    iva_tipo = tipo_iva()
    iva = operacion(importe, iva_tipo)
    final(importe, iva)

if __name__ == "__main__":
    main()

