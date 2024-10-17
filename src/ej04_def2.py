
def grados_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    return celsius  

def main():
    fahrenheit = float(input("Introduce la temperatura en grados Fahrenheit: "))
    temperatura = grados_celsius(fahrenheit)
    print(f"{temperatura:.2f}ºC")  
    
if __name__ == "__main__":
    main()



    