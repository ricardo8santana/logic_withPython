login = input("Digite seu login:")
senha = input ("Digite sua senha:")

if  login == "aluno" and senha == "123":
    print(login)
else:
    login = input("Digite sua login:")
    senha = input("Digite sua senha:")

while login != "aluno" or senha != "123":
    print("acesso negado!")
    login = input("Digite sua login:")
    senha = input("Digite sua senha:")
print("Login realizado!")