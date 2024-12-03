'''
Desenvolva um programa que permita calcular o valor total das inscrições para um evento, aplicando um desconto de 15% para inscrições realizadas em grupo (3 ou mais pessoas) e exibindo o valor total para inscrições individuais. O programa deverá fazer uso de laços de repetição e funções para estruturar as operações.

Descrição:
O programa deve começar solicitando ao usuário o número de pessoas do grupo ou uma inscrição individual.
Para cada pessoa, o programa deve receber o nome, o tipo de ingresso (normal ou VIP) e o valor do ingresso:
O ingresso normal custa R$ 100,00.
O ingresso VIP custa R$ 200,00.
Ao final, o programa calculará o valor total das inscrições.
O cliente poderá escolher a forma de pagamento entre cartão de crédito, boleto ou débito.
Se a inscrição for para um grupo (3 ou mais pessoas), o programa deve aplicar um desconto de 15% sobre o valor total.
Se a inscrição for individual, não haverá desconto.
Se o pagamento for em cartão de crédito, o programa deverá perguntar em quantas parcelas o cliente deseja dividir o valor. O valor de cada parcela será calculado, sem juros adicionais.
O programa deve exibir o valor total da inscrição, o valor do desconto (se aplicável) ou o valor das parcelas (se for no crédito), conforme o tipo de pagamento.
'''
def calcular_desconto(valor_total, num_pessoas):
    if num_pessoas >= 3:
        desconto = valor_total * 0.15
        valor_total = valor_total - desconto
        return valor_total, desconto
    else:
        return valor_total, 0
def calcular_valor_ingresso(tipo_ingresso):
    if tipo_ingresso.lower() == 'normal':
        return 100
    elif tipo_ingresso.lower() == 'vip':
        return 200
    else:
        print("Tipo de ingresso inválido! Considerando ingresso normal.")
        return 100
def calcular_parcelas(valor_total):
    parcelas = int(input("Em quantas parcelas você deseja dividir? "))
    valor_parcela = valor_total / parcelas
    print(f"Valor total: R${valor_total:.2f}")
    print(f"Parcelas de R${valor_parcela:.2f} sem juros.")
    return valor_parcela
# Solicita o número de pessoas no grupo ou se é uma inscrição individual
num_pessoas = int(input("Quantas pessoas estão se inscrevendo? "))
total_valor = 0  # Variável para somar o valor total das inscrições
for i in range(num_pessoas):
    print(f"\nInscrição da pessoa {i + 1}:")
    nome = input("Digite o nome da pessoa: ")
    tipo_ingresso = input("Digite o tipo de ingresso (normal ou vip): ").strip().lower()
    
    valor_ingresso = calcular_valor_ingresso(tipo_ingresso)
    total_valor = total_valor + valor_ingresso
    
# Calcular o valor total e aplicar o desconto, se aplicável
total_valor, desconto = calcular_desconto(total_valor, num_pessoas)
print(f"\nValor total das inscrições (antes do desconto): R${total_valor + desconto:.2f}")
if desconto > 0:
    print(f"Desconto aplicado: R${desconto:.2f}")
# Pergunta o tipo de pagamento
tipo_pagamento = input("\nEscolha o método de pagamento (1 - cartão de crédito, 2 - boleto, 3 - débito): ").strip().lower()
if tipo_pagamento == '1':
    # Se for cartão de crédito, perguntar o número de parcelas
    calcular_parcelas(total_valor)
elif tipo_pagamento == '2' or tipo_pagamento == '3':
    print(f"\nValor total a ser pago: R${total_valor:.2f}")
else:
    print("Método de pagamento inválido.")
