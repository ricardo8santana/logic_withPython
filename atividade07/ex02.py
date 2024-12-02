# 1Crie um programa que contenha uma lista com os números [2, 4, 6, 8] e use um laço for para calcular #
# e imprimir o dobro de cada número dessa lista. 
lista = [2, 4, 6, 8]

for numero in lista:
    print(numero * 2)

# 2Crie um programa que contenha uma lista de números inteiros. Utilize um laço for para percorrer a lista e encontrar o maior número. 
# O programa deve imprimir o maior número da lista. Exemplo de lista: [3, 5, 7, 2, 8, 1] 
lista_numeros = [3, 5, 7, 2, 8, 1]
maior = lista_numeros[0]

for numero in lista_numeros:
    if numero > maior:
        maior = numero
print("O maior número da lista é:", maior)


# 4 Crie um programa que contenha uma lista com os números de 1 a 5.
#  Utilize um laço for para criar uma nova lista com o quadrado de cada número dessa lista original.
#  O programa deve imprimir a nova lista. 
#  Exemplo de lista original: [1, 2, 3, 4, 5] Resultado esperado: [1, 4, 9, 16, 25]

lista =list(range(1, 6))

for numero in lista:
    lista_numeros.append(numero**2)
print(lista_numeros)


#5Crie um programa que leia o nome escrito pelo usuário e pergunte qual a letra ele quer verificar.
# O programa deve dizer se a letra existe e qual a quantidade.

nome = input("Digite seu nome: ")

letra = input("Digite a letra que você quer verificar: ")

contador = 0

for letra in nome:
    if letra.upper() == letra.upper():
        #print('Letra encontrada')
        contador = contador + 1

if contador > 0:
    print(f"A letra '{letra}' aparece {contador} vez(es) no seu nome.")
else:
    print(f"A letra '{letra}' não aparece no seu nome.")

    # palavra = 'PyThON'
# palavra_maiuscula = palavra.upper()
# palavra_minuscula = palavra.lower()

# print(palavra)
# print(palavra_minuscula)
# print(palavra_maiuscula)
