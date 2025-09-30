# Coleção não ordernada de pares, chaves, valor
#> não ordernada =! da tupla e da lista

# Criando um dicionário de exemplo

pessoa = {"nome": "Thaís", "idade": 30, "cidade": "Belo Horizonte"} #chave nome com o valor João...

# Exibindo o dicionário
print("Meu dicionário:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

# Pode adicionar quantas chaves quiser
pessoa["sobrenome"] = "Moreira"
print("Sobrenome", pessoa["sobrenome"])
print("Meu dicionário:", pessoa)

# Atualizando um valor
pessoa["idade"] = 31
print("Idade atualizada:", pessoa["idade"])
print("Meu dicionário:", pessoa)

# Removendo um par chave-valor
del pessoa["sobrenome"]
print("Meu dicionário:", pessoa)

# # Métodos: keys(), values(), items()
# chaves = pessoa.keys()
# print("Chaves do dicionário", chaves)
# print("Primeira chave:", chaves[0]) > tentando ascessar os elementos individualmente como em uma lista
#> pode retornar um erro porque nao essa keys não é uma lista direta, ai tem que transformar em lista como abaixo:

chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

# # Métodos values
# valores = pessoa.values()
# print("Valores do dicionário:", valores)
# # print("Primeira valor:", valor[0]) > tentando ascessar os elementos individualmente como em uma lista
# #> pode retornar um erro porque nao esse valor não é uma lista direta, ai tem que transformar em lista como abaixo:

valores = list(pessoa.values())
print("Valores do dicionário:", valores)
print("Primeiro valor do dicionário:", valores[0])

# Métodos items
itens = pessoa.items()
print("Pares chave-valor do dicionário:", itens)
print(type(itens))

itens = list(pessoa.items())
print("Convertendo dict para list", type(itens))
print("Primeira chave-valor: %s = %s" %(itens[0][0], itens[0][1]))
print("Segunda chave-valor: {} = {}".format(itens[1][0], itens[1][1]))