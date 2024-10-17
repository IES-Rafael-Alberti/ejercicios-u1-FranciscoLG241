
def introducir_temperatura():
    fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
    return fahrenheit

def convertir_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    return celsius

def resultado(fahrenheit, celsius): 
    resultado = f"{celsius:.2f}ºC ({fahrenheit:.2f}ºF)"
    return resultado

def main():
    temp1 = introducir_temperatura()
    temp2 = convertir_a_celsius(temp1)
    fin = resultado(temp1, temp2)
    print(f"La temperatura en grados Fahrenheit es {fin}")
    
if __name__ == "__main__":
    main()
