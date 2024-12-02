def exibeNome(name):
    return print(f"Good Morning Welcome!, {name}")

def leNome():
    nome = input("Digite seu nome:")
    return nome

#Chama a função leName para gurdar o name de um usuário e guarda na variável n
n = leNome

#Chama a função a função displayName usando o name que foi armazenado na variável n
exibeNome(n)

def exibeNome(name):
    return print(f"Good Morning Welcome!, {name}")

def leDado(tipo, texto):
    if tipo == 'str':
        dado = input(texto)
    elif tipo == 'int':
        dado = int(input(texto))
    elif tipo == 'float':
        dado = float(input(texto))
    return dado

#Chama a função leName para gurdar o name de um usuário e guarda na variável n
n = leDado('str', "Digite o seu nome:")
idade = leDado('int', "Digite o sua  idade:")

# exibeNome("Louis")
# exibeNome("Richard")

