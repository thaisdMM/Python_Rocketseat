# Declaraçao de lista

minha_lista = [5, 1, 4, "Maria", True, False]

# Exibindo a lista
print("Minha lista de exemplo: ", minha_lista)

# Exibindo ítem específico da lista
print("minha_lista[0]:", minha_lista[0])
print("minha_lista[3]:", minha_lista[3])

# Fatiando a lista do índice 1 a 5
print("minha_lista[1:5]:", minha_lista[1:5])

# Fatiando a lista do começo ao índice desejado
print("minha_lista[:4]:", minha_lista[:4])

# Fatiando a lista de um elemento até o final
print("minha_lista[2:]:", minha_lista[2:])

# Mudando elementos da lista
minha_lista[0] = "python"
print(minha_lista)

## Método append(): Adiciona um elemento ao final da lista
minha_lista.append(6)
print("Após append(6)", minha_lista)

# Método index procura em que índice está um item da sua lista
indice = minha_lista.index("Maria")
print("Indice do elemento Maria:", indice)

# Método insert: Insere um elemento após um índice específico
minha_lista.insert(3, "João")
print("Após o índice indicado(3) insert(João) minha_lista.insert(3, 'João'):", minha_lista)

# Método pop - REMOVE o elemento indicado
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print("Após pop(3):", minha_lista)

# Método remove - REMOVE o primeiro elemento que vc declarou, se tiverem outros nao remove
#Em Python, os valores True e False são tratados como 1 e 0, respectivamente. Isso significa que, dentro de uma lista, se houver o número 1, o Python o considera equivalente a True.
#> Quando printei o metodo remove a resposta foi: Após remove(True): ['python', 4, 'Maria', True, False, 6]
#>> tirou o 1 da lista e nao o True

minha_lista.remove(True)
print("Após remove(True):", minha_lista)

# Método sort nao dá certo se a lista tem vários elementos: int, str, bool; pode dar erro tb pq a lista foi modificada
# rodar uma lista nova para dar certo
minha_lista = [1, 10, 3, 3, 5, 6, 7, 8, 112]
print(minha_lista)
minha_lista.sort()
print("Após sort()", minha_lista)

# Resposta do código executado no terminal

# Minha lista de exemplo:  [5, 1, 4, 'Maria', True, False]
# minha_lista[0]: 5
# minha_lista[3]: Maria
# minha_lista[1:5]: [1, 4, 'Maria', True]
# minha_lista[:4]: [5, 1, 4, 'Maria']
# minha_lista[2:]: [4, 'Maria', True, False]
# ['python', 1, 4, 'Maria', True, False]
# Após append(6) ['python', 1, 4, 'Maria', True, False, 6]
# Indice do elemento Maria: 3
# Após o índice indicado(3) insert(João) minha_lista.insert(3, 'João'): ['python', 1, 4, 'João', 'Maria', True, False, 6]
# Elemento removido: João
# Após pop(3): ['python', 1, 4, 'Maria', True, False, 6]
# Após remove(True): ['python', 4, 'Maria', True, False, 6]
# [1, 10, 3, 3, 5, 6, 7, 8, 112]
# Após sort() [1, 3, 3, 5, 6, 7, 8, 10, 112]