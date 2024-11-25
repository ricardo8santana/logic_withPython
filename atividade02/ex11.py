val1 = float (input("Digite o 1º lado do triangulo:"))
val2 = float (input("Digite o 2º lado do triangulo:"))
val3 = float (input("Digite o 3º lado do triangulo:"))

if val1 <= 0 or val2 <= val3 <= 0:
    print("Não é um triângulo")
elif val1 + val2 > val3 and val2 + val2 + val3 > val1 and val1 + val3 > val2:
    print("Não é um triângulo ")
elif val1 == val2 == val3:
    print("Triângulo Equilatero")
elif val1 != val2 != val3:
    print("Triangulo Escaleno")
elif val1 == val2 or val1 == val3 or val2 == val3:
    print("Triângulo Isósceles")