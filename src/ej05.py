importe = float(input("Introduza el importe del IVA del artículo: "))
iva = float(input("Introduce el % de IVA aplicar: "))
if (iva < 0 or iva > 100):
        iva = 21
        print("El porcentaje debe de ser en 0 y 100")
importe_con_iva = importe + importe * (iva / 100)
importe_con_iva = round(importe_con_iva,2)
print("El precio final del artículo es de {importe_con_iva}")

