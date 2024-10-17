precio = input("Introduce el precio del producto en euros con dos decimales: ")
euros = precio.split(".")[0]
centimos = precio.split(".")[1]
print(f"El numero de euros sería de {euros} y el número de centimos seria de {centimos}")
