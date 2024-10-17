precio = float(input("Introduzca el importe final: "))
iva_aplicado = float(input("Introduce el IVA aplicado: "))
iva_aplicado /= 100
precio_sin_iva = precio / (1 + iva_aplicado)
iva_calculado = precio - precio_sin_iva
precio_sin_iva = round(precio_sin_iva,2)
print("Precio sin IVA: ")