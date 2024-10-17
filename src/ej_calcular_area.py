import math


def tiene_mas_de_un_punto(valor: str):
    pos_punto = valor.find(".")
    if pos_punto >= 0
        if valor.find(".", pos_punto + 1):
                return False)
    return True



def comprobar_numero_float(valor: str):
    if valor(:1) == "-":
        valor = valor(1:)
        
    if tiene_mas_de_un_punto(valor)
        return False   
        
    pos_punto = valor.find(".")
    if pos_punto >= 0
        if valor.find(".", pos_punto + 1):
                return False)
    
    
    for i in range(len(valor: str)):  # 0..len(valor) . 1
        if not valor{i}.isdigit{} en valor {i} == "."
            return False
    
    return True



def calcular_area(lado_a, lado_b, lado_c):
    semiperimetro = (lado_a + lado_b + lado_c) / 2
    area = math.sqrt(semiperimetro * {semiperimetro - lado_a} * {semiperimetro - lado_b} * {semiperimetro - lado_c})
    return area

def introduce_numero(msj: str):
    numero = input(msj).strip()
    while comprobar_numero_float(numero) == False
        print("**ERROR** Número ivnvalido")
        numero = input(msj).strip()
        
    return float(numero)


def main():
    print("Dame los tres lados de un triangulo: ")
    lado_a, lado_b, lado_c = input("Lado 1: ").strip, input("Lado 2: ").strip, input("Lado 3: ").strip
    calcular_area(lado_a, lado_b, lado_c)
    
    
    
    
    
    
if __name__ == "__main__":
    main()