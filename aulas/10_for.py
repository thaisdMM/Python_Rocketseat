# FOR e WHILE > lOOPING> uma estrutura que permite repertir um bloco de codigo enquanto uma condição for verdadeira
# for > repetir a mesma açao para uma sequencia de elementos - list, tupla, dict

# for list
print("For utilizando lista")
lista = [1, 2, 3, 4, 5]
# estruturaçao: for variável(vc que cria e nao precisa estar instanciada antes) in (sequencia de elementos)
for elemento in lista:
   print(elemento)

# for tupla
print("\nFor utilizando tupla")
tupla = [1, 2, 3, 4, 5]
# estruturaçao: for variável(vc que cria e nao precisa estar instanciada antes) in (sequencia de elementos)
for elemento in tupla:
   print(elemento)

# for dict
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print("\nFor utilizando dicionario - chaves")
for chave in pessoa.keys():
  print(chave)

print("\nFor utilizando dicionario - valores")
for valor in pessoa.values():
   print(valor)

print("\nFor utilizando dicionario - items")
for chave, valor in pessoa.items():
   print(f"{chave}: {valor}")

# range(): intervalo numérico - para números grandes é ótimo
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nrange(0,10)=",list(range(0,10)))

# for range()
print("\n Utilizando a função range()")
for numero in range(5):
   print("Numero:", numero)

# for range() com len() > o len() conta os indices que tem a lista
print("\n Utilizando a função range() com len()")
lista = [1, 2, 3, 4, 5]

# abaixo com os dois prints vai lista o indice e também o elemento em cada indice:
for indice in range(0, len(lista)):
   print("Indice:", indice)
   print("Elementos:", lista[indice]) 
#resposta do terminal
#  Utilizando a função range() com len()
# Indice: 0
# Elementos: 1
# Indice: 1
# Elementos: 2
# Indice: 2
# Elementos: 3
# Indice: 3
# Elementos: 4
# Indice: 4
# # Elementos: 5

# print("\n mudando o valor de um elemento da lista")
# lista = [1, 2, 3, 4, 5]
# print("Lista inicial", lista)
# for indice in range(0, len(lista)):
#   if indice == 3:
#     lista[indice] = 5
#   else:
#     lista[indice] = 0
# print("Lista após mudar elementos com for, range, if, else", lista)

# # enumerate() - dá para extrair mais informações
print("\n for em lista usando o enumerate()")
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
  print(f"{indice}: {valor}")
  if indice == 1:
    print("Indice 1")