def totalCompras(precos):
    total = 0 
    for preco in precos:
        total = preco + total
    return total

def desconto(total, pagamento):
    if pagamento == 1 or pagamento == 2: #pix ou débito 
        desconto = total * 0.05
        total_desconto = total - desconto
        return total_desconto
    else:
        return total, 0 #no caso do crédito, não tem desconto
    
def parcelamento(total, parcelas):
    valor_parcela = total / parcelas
    return valor_parcela

n = int(input("Quantos produtos vai comprar?"))

produtos = []
precos = []

for i in range(n):
    nome = input("Nome do produto:")
    preco = float(input("Valor do produto:"))
    produtos.append(nome)
    precos.append(preco)

total = totalCompras(precos)
print("O total da compra foi:", total)

print("Escolha a forma de pagamento:")
print("1 - Pix")
print("2 - Débito")
print("3 - Crédito")
pagamento = int(input("Escolha a forma de pagamento:"))

if pagamento == 1 or pagamento == 2:
    valorComDesconto = desconto(total, pagamento)
    print(f"Você recebeu 5% de desconto")
    print(f"Seu desconto foi de R${(total-valorComDesconto):.2f}")
    print(f"O valor final é R$ {valorComDesconto:.2f}")
elif pagamento == 3:
    parcelas = int(input("Em quantas parcelas deseja dividir?"))
    valorParcela = parcelamento(total, parcelas)
    print(f"O valor de cada parcela será de R$ {valorParcela:.2f} em {parcelas} parcelas")
else:
    print("Opção inválida")