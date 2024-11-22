saldoConta = float(input("Qual o saldo da conta:"))
valorProduto = float(input("Qual o valor da produto"))

if saldoConta >= valorProduto:
    result = "pode comprar o produto"
else:
    result = " não tem saldo sufuciente"

    print(result)

