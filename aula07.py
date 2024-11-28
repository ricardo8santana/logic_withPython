#Imprimindo todos os itens da lista
lista = [1, 2, 3, 4, 5]
lista_frutas = ["Maçã", "Uva", "Banana"]

for numero in lista:
    print(numero ** 2)

    verifica = False

for fruta in lista_frutas:
    if fruta == "Maçã":
     verifica = True
    if verifica == True:
     print("Fruta encontrada")
else:
   print("Fruta não encontrada")

# else:
#     print("Não exite essa fruta na lista")

# for numero in range(1, 101):
#    print(numero)

nome = "Maria"
verf = False
c = 0

for letra in nome:
   if letra == 'a':
      verf = True
      c = c + 1

if verf == True:
   print("Existe a letra A no nome e existe", c, "letras")
else:
   print("Letra A não existe")
