
importe_sin_iva = float(input("Introduce el importe sin IVA del artículo: "))
tipo_iva = float(input("Introduce el tipo de IVA a aplicar (en porcentaje): "))
iva = (tipo_iva / 100) * importe_sin_iva
precio_final = importe_sin_iva + iva
print(f"El precio final del artículo es: {precio_final:.2f}€")


