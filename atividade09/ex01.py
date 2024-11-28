#1 Crie um programa que contenha uma lista de numeros inteiros e utilizando um laço for,
#  calcule e imprima a soma de todos os números dessa lista Exemplo de lista:[3, 5, 7, 2, 8, 1].
# Resultado esperado: 26 (porque 3 + 5 + 7 + 2 + 8 + 1 = 26
numero = [3, 5, 7, 2, 8, 1]
soma = 0
for numero in numero:
    soma += numero
    print(f'A soma de todos os números na lista é:{soma}' )

# 2 Crie um programa que contenha uma lista de números inteiros de 1 a 20 (usando o range).
#  Utilize um laço for para criar uma nova lista contendo apenas os números pares da lista original e imprima essa nova lista.
lista_numero = []

for numero in range(1, 21):
    lista_numero = numero
    print(lista_numero)


#3 Crie um programa que contenha uma lista com alguns números inteiros, positivos e negativos.
#  Utilize um laço for para contar quantos números negativos existem na lista e imprima essa quantidade.
numeros = [10, -5, 3, -2, 8, -1, 0, -7, 12]

quantidade_negativos = 0
for numero in numeros:
    if numero < 0:  
        quantidade_negativos += 1  
print(f'A quantidade de números negativos na lista é: {quantidade_negativos}')

#4  Crie um programa que contenha uma lista de números inteiros. 
# Utilize um laço for para criar uma nova lista com os elementos da lista original, mas na ordem inversa, e imprima essa nova lista.
lista = [2, 3, 6, 5, 4]

lista_inteiros = 0
for numero in lista:
    if numero  > 0:
       lista_inteiros.reverse()
print(f'Lista de numeros inteiros é:{lista_inteiros} ')


#5  Crie um programa que leia uma string fornecida pelo usuário e, utilizando um laço for,
#  conte quantas vogais (a, ais (a, e, i, o, u) existem nessa string. O programa deve imprimir o total de vogais encontradas.
# Lê uma string fornecida pelo usuário
texto = input("Digite uma frase ou palavra: ")

contagem_vogais = 0
vogais = "aeiouAEIOU"

for caractere in texto:
    if caractere in vogais:  
        contagem_vogais += 1  
print(f'Total de vogais encontradas: {contagem_vogais}')

