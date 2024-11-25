valor1 = float(input("Digite um numero:"))
valor2 = float(input("Digite outro numero:"))

print("Qual operação")
operacao = input("Esccolha -> + | - |*| / :")

if operacao == '+':
    resultado = valor1 + valor2
elif  operacao == '-':
    resultado = valor1 - valor2
elif  operacao == '*':
    resultado = valor1 * valor2
elif  operacao == '/':
    resultado = valor1 / valor2    
else:
    resultado = "Operação invalida!"
print(resultado)