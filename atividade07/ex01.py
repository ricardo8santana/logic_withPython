produtros = ["Arroz", "Feijão", "Óleo", "Açúcar", "Macarrão"]
quantidades = [10, 25, 5, 20, 15]

#1Exibindo a lista completa
print(f'\n{'#*'*80}\n')
print(produtros)
print(quantidades)

#2Acessando e Imprimindo  a lista completa
print(f'\n{'#*'*80}\n')
print("Acessando o primeiro nome da lista produtos:", produtros[0])
print("Acessando o segunda nome da lista quantidades:", quantidades[1])

#3Acessando e Imprimindo  a lista completa
print(f'\n{'#*'*80}\n')
print("Tamanho da lista produtros:", len(produtros)) # len(nomes)
print("Tamanho da lista quantidades:", len(quantidades))




#4Modificando a quantidade do terceiro produto para um novo valor imprima a lista
print(f'\n{'#*'*80}\n')
print("Quantidades sem  moficação:", quantidades)
quantidades.insert(3, 30)
print("Quantidades após  moficação:", quantidades)

#5Adicione um novo produto ex: Sal
print(f'\n{'#*'*80}\n')
print("Produto sem modificação:", produtros)
 #adicionando um novo nome na lista nomes na última posição
produtros.append("Sal")
print("Produtos após modificação:", produtros)

#6Insira um novo produto ex: Café, com qtd 10 na segunda posição
#indice1 da lista produtos e quantidades e imprima as lista apos a inserção

print(f'\n{'#*'*80}\n')

print("Produtos sem  moficação:", produtros)
#insere um novo item nalista baseada na posição
#insere (posição, valor)
produtros.insert("Café", 10)
print("Produtos após  moficação:", produtros)

print(f'\n{'#*'*80}\n')

#7Remova um produto da lista produtos pelo nome ex:"Feijão" e imprima a lista de produtos atulizadas 
print("Produtos sem modificação:", produtros)
 #Removendo um item valor da lista
produtros.remove("Feijão")
print("Produtos após modificação:", produtros)

#8Remova um produto da lista quatidades baseado na posição ex: remover o produto na posição 2 e imprimei
print(f'\n{'#*'*80}\n')

print("Quantidades sem  moficação:", quantidades)
#Removendo um item por posição da lista
quantidades.pop(2)
print("Quantidades após  moficação:", quantidades)

#9 Ordene a lista de produtos em ordem alfabética e imprima a lista ordenada
print(f'\n{'#*'*80}\n')

print("Produtos sem ordenação:", produtros)
produtros.sort() 
print("Produtos após ordenação:", produtros)

#10 Inverta a lista de quatidades e imprima a lista de quantidade após a reversão
print(f'\n{'#*'*80}\n')

print("Quantidades sem reversão:", quantidades)
quantidades.reverse()
print("Quantidades após a reversão:", quantidades)

#11 Localize a posição de um produto especifico na lista produtos e imprima o indíce em que o produto se encontra
print(f'\n{'#*'*80}\n')

print("Lista nomes:", produtros)
#index() retorna a posição em que o valor está localizado
cafe = produtros.index("Café")
print("Café esta na posição", cafe) 