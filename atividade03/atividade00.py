anoAtual = int(input("Digite o ano atual:"))
idade = int(input("Digite sua idade: "))

fezAniversario = 2024(input("Fez aniversario esse ano ? (True/False)"))

if fezAniversario == 'sim':
    ano = anoAtual - idade
else:
    ano = anoAtual - 1 - idade

print("Você nasceu em ", ano)