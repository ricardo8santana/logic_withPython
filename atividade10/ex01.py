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

n = int(input("Quantos produtos va i comprar?"))

produtos = []
precos = []

for i in range(n):
    nome = input("Nome do produto:")
    preco = float(input("Valor do produto"))
    produtos.append(nome)
    precos.append(preco)

total = totalCompras(precos)
print("O total da compra foi:", total)