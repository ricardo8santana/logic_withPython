#1 Crie um programa que contenha uma lista de numeros inteiros e utilizando um laço for,
#  calcule e imprima a soma de todos os números dessa lista Exemplo de lista:[3, 5, 7, 2, 8, 1].
# Resultado esperado: 26 (porque 3 + 5 + 7 + 2 + 8 + 1 = 26
numero = [3, 5, 7, 2, 8, 1]
soma = 0
for numero in numero:
    soma + numero
    print(soma)

# 2 Crie um programa que contenha uma lista de números inteiros de 1 a 20 (usando o range).
#  Utilize um laço for para criar uma nova lista contendo apenas os números pares da lista original e imprima essa nova lista.
lista = list(range(1, 21))
lista_numero = []

for numero in lista:
    if numero%2 == 0:
      lista_numero.append(numero)

    print(lista_numero)


#3 Crie um programa que contenha uma lista com alguns números inteiros, positivos e negativos.
#  Utilize um laço for para contar quantos números negativos existem na lista e imprima essa quantidade.
numeros = [10, -5, 3, -2, 8, -1, 0, -7, 12]

quantidade_negativos = 0
for numero in numeros:
    if numero < 0:  
        quantidade_negativos = quantidade_negativos + 1  
print(f'A quantidade  {quantidade_negativos} de números negativos na lista é: {numeros}')

#4  Crie um programa que contenha uma lista de números inteiros. 
# Utilize um laço for para criar uma nova lista com os elementos da lista original, mas na ordem inversa, e imprima essa nova lista.
lista = [2, 1, 3, 6, 5, 4, 10]
lista_reverse = []

#tam = len(lista)

for numero in lista:
   # if numero  > 0:
       lista_reverse.insert(0, numero)
       #tam = tam -1
print(lista_reverse)


#5  Crie um programa que leia uma string fornecida pelo usuário e, utilizando um laço for,
#  conte quantas vogais (a, ais (a, e, i, o, u) existem nessa string. O programa deve imprimir o total de vogais encontradas.
# Lê uma string fornecida pelo usuário

# texto = input("Digite uma frase ou palavra: ")

# contagem_vogais = 0
# vogais = "aeiouAEIOU"

# for caractere in texto:
#     if caractere in vogais:  
#         contagem_vogais += 1  
# print(f'Total de vogais encontradas: {contagem_vogais}')

palavra = input("Digite uma palavra:")

a = 0
e = 0
i = 0
o = 0
u = 0

for letra in palavra:
    if letra.lower() == 'a':
        a = a + 1
    elif letra.lower() == 'e':
     e = e  + 1
    elif letra.lower() == 'i':
     i = i + 1
    elif letra.lower() == 'o':
     o = o  + 1
    elif letra.lower() == 'u':
     u = u  + 1
print(f"Foram encontradas:\n A:{a} \n E:{e} \n I:{i} \n O:{o} \n U:{u}")