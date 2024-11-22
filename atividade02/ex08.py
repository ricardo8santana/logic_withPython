jg1 = input("Jogador 1 \ pedra, papel, ou tesoura:")
jg2 = input("Jogador 2 \ pedra, papel, ou tesoura:")

#verifica empate
if jg1 == jg2:
    print("Empate")
    '''
if jg1 == "tesoura" and jg2 == "tesoura":
    print("Empate")
elif jg1 == "pedra" and jg2 == "pedra":
    print("Empate")
elif jg1 == "papel" and jg2 == "papel":
    print("Empate")
    '''

#verifica jogador 1
elif jg1 == "pedra" and jg2 == "tesoura":
    print("Jogador 1 venceu!")


#verifica jogador 2
else:
    print("Jogador 2 venceu!")