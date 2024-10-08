productos = input("Introduce los productos de la compra, separado por comas: ")
lista_productos = productos.split(",")

print("\nProductos en la cesta de la compra: ")
for productos in lista_productos:
    print(productos.strip())
    