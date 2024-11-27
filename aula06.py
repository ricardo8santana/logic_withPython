nomes = ["Ana", "João", "Paula", "Matheus"]
idades = [18, 26, 15, 25]

#exibindo a lista completa
print(nomes)
print(idades)

#Quebra de linha e separação com #
print(f'\n{'#*'*80}\n')

print("Acessando o primeiro nome da lista nomes:", nomes[0])
print("Acessando o segunda nome da lista idades:", nomes[1])

print(f'\n{'#*'*80}\n')

# O tamanho da lista é retornado pela função len()

print("Tamanho da lista nomes:", len(nomes)) # len(nomes)
print("Tamanho da lista idades:", len(idades)) # len(idades)

#Quebra de linha e separação com #
print(f'\n{'#*'*80}\n')

print("Idades sem modificação", idades)
idades[2] = 16 #alterando o valor da posição 2 para 16
print("Idades após a modificação:", idades)

#Quebra de linha e separação com #
print(f'\n{'#*'*80}\n')

print("Nomes sem modificação:", nomes)
 #adicionando um novo nome na lista nomes na última posição
nomes.append("Carlos")
print("Nomes após modificação:", nomes)

#Quebra de linha e separação com #
print(f'\n{'#*'*80}\n')

print("Idades sem  moficação:", idades)
#insere um novo item nalista baseada na posição
#insere (posição, valor)
idades.insert(1, 50)
print("Idades após  moficação:", idades)

#Quebra de linha e separação com #
print(f'\n{'#*'*80}\n')

print("Nomes sem modificação:", nomes)
 #Removendo um item valor da lista
nomes.remove("Ana")
print("Nomes após modificação:", nomes)

#Quebra de linha e separação com #
print(f'\n{'#*'*80}\n')

print("Idades sem  moficação:", idades)
#Removendo um item por posição da lista
idades.pop(2)
print("Idades após  moficação:", idades)

#Quebra de linha e separação com #
print(f'\n{'#*'*80}\n')

print("Nomes sem ordenação:", nomes)
 #Para ordenar uma lista usamos o sort() (alfabetica ou númerica)
nomes.sort() #sort(reverse=True)
print("Nomes após ordenação:", nomes)

#Quebra de linha e separação com #
print(f'\n{'#*'*80}\n')

print("Idades sem reversão:", idades)
 #Para reverter uma lista usamos o reverse() 
idades.reverse()
print("Idades após a reversão:", idades)

#Quebra de linha e separação com #
print(f'\n{'#*'*80}\n')

print("Lista nomes:", nomes)
#index() retorna a posição em que o valor está localizado
iPaula = nomes.index("Paula")
print("Paula esta na posição", iPaula)








