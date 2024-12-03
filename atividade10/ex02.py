

def calcular_valor_ingresso(tipo_ingresso):
    """Função para calcular o valor do ingresso com base no tipo escolhido."""
    if tipo_ingresso == 'normal':
        return 100.00
    elif tipo_ingresso == 'VIP':
        return 200.00
    else:
        print("Tipo de ingresso inválido!")
        return 0

def calcular_desconto(valor_total, num_pessoas):
    """Função para aplicar o desconto de 15% se o número de pessoas for 3 ou mais."""
    if num_pessoas >= 3:
        return valor_total * 0.15
    else:
        return 0

def calcular_parcelas(valor_total, num_parcelas):
    """Função para calcular o valor de cada parcela, se o pagamento for no cartão de crédito."""
    if num_parcelas > 0:
        return valor_total / num_parcelas
    else:
        return 0

def obter_tipo_pagamento():
    """Função para solicitar o tipo de pagamento ao usuário."""
    while True:
        tipo_pagamento = input("Escolha o tipo de pagamento (cartão de crédito, boleto, débito): ").lower()
        if tipo_pagamento in ['cartão de crédito', 'boleto', 'débito']:
            return tipo_pagamento
        else:
            print("Opção inválida! Tente novamente.")

def obter_numero_parcelas():
    """Função para solicitar o número de parcelas, se o pagamento for no cartão de crédito."""
    while True:
        try:
            num_parcelas = int(input("Quantas parcelas você deseja (0 para pagamento à vista)? "))
            if num_parcelas >= 0:
                return num_parcelas
            else:
                print("Número de parcelas deve ser 0 ou maior.")
        except ValueError:
            print("Valor inválido! Digite um número inteiro.")

def calcular_inscricao():
    """Função principal que gerencia o cálculo de inscrição para evento."""
    # Solicitar número de pessoas
    num_pessoas = int(input("Digite o número de pessoas no grupo (1 para individual): "))
    
    total_valor = 0.0

    # Laço para cadastrar cada pessoa
    for i in range(num_pessoas):
        print(f"\nPessoa {i+1}:")
        nome = input("Digite o nome da pessoa: ")
        tipo_ingresso = input("Digite o tipo de ingresso (normal ou VIP): ").lower()
        valor_ingresso = calcular_valor_ingresso(tipo_ingresso)
        total_valor += valor_ingresso
        print(f"Valor do ingresso de {nome}: R$ {valor_ingresso:.2f}")

    # Calcular o desconto, se aplicável
    desconto = calcular_desconto(total_valor, num_pessoas)
    total_com_desconto = total_valor - desconto

    # Exibir o valor com ou sem desconto
    if num_pessoas >= 3:
        print(f"\nDesconto aplicado (15%): R$ {desconto:.2f}")
        print(f"Total com desconto: R$ {total_com_desconto:.2f}")
    else:
        print(f"\nTotal sem desconto: R$ {total_valor:.2f}")

    # Escolher forma de pagamento
    tipo_pagamento = obter_tipo_pagamento()

    if tipo_pagamento == "cartão de crédito":
        num_parcelas = obter_numero_parcelas()
        parcelas = calcular_parcelas(total_com_desconto, num_parcelas)
        print(f"Total das parcelas: R$ {parcelas:.2f} por {num_parcelas} parcela(s).")
    else:
        print(f"Pagamento efetuado via {tipo_pagamento}.")

def main():
    """Função principal para iniciar o programa."""
    print("Bem-vindo ao sistema de inscrição para o evento!")
    calcular_inscricao()

if __name__ == "__main__":
    main()

        









    '''
        Desenvolva um programa que permita calcular o valor total das inscrições para um evento, 
        aplicando um desconto de 15% para inscrições realizadas em grupo (3 ou mais pessoas)
          e exibindo o valor total para inscrições individuais. O programa deverá fazer uso de
            laços de repetição e funções para estruturar as operações.
        
        
        Descrição:
        
            O programa deve começar solicitando ao usuário o número de pessoas do grupo ou uma inscrição individual.
            Para cada pessoa, o programa deve receber o nome, o tipo de ingresso (normal ou VIP) e o valor do ingresso:
                O ingresso normal custa R$ 100,00.
                O ingresso VIP custa R$ 200,00.
            Ao final, o programa calculará o valor total das inscrições.
            O cliente poderá escolher a forma de pagamento entre cartão de crédito, boleto ou débito.
            Se a inscrição for para um grupo (3 ou mais pessoas), o programa deve aplicar um desconto de 15% sobre o valor total.
            Se a inscrição for individual, não haverá desconto.
            Se o pagamento for em cartão de crédito, o programa deverá perguntar em quantas parcelas o cliente deseja dividir o valor. 
            O valor de cada parcela será calculado, sem juros adicionais.
            O programa deve exibir o valor total da inscrição, o valor do desconto (se aplicável) ou o valor das
              parcelas (se for no crédito), conforme o tipo de pagamento.
        '''