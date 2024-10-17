def main():
    telefono = input("Introduce un número de teléfono (+34-número-extensión): ")
    telefono = telefono.split('-')[1]
    print(f"Tu número de telefono sin extensiones es {telefono}")
  
if __name__ == "__main__":
    main()

