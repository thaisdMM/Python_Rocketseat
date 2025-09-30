# Tupla: coleção ordenada e imutável de elementos 
#> diferente da lista, a tupla depois de declarada não pode mudar os elementos dela

# Criando uma tupla de ex

minha_tupla = (1,2, 2,3,4)

print("Minha tupla:", minha_tupla)

print("minha_tupla[0]:", minha_tupla[0])
print("minha_tupla[2]:", minha_tupla[2])
print("minha_tupla[-1] acessa o último elemento da tupla:", minha_tupla[-1])

# Método count - retorna a quantidade de vezes que um elemento aparece na tupla
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", contagem)

indice = minha_tupla.index(4)
print("Indice da primeira ocorrência do elemento 4:", indice)
