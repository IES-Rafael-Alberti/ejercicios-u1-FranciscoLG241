nombre = input("Introduce el nombre del producto: ")
precio = float(input("Introduce su precio: "))
unidades = int(input("Introduce el numero de unidades: "))

precio_total = precio * unidades

print(f"El producto que ha comprado es {nombre}, su precio es de{precio:6.2f} con una cantidad de {unidades} y un coste total de{precio_total:8.2f}")
