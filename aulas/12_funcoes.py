# com a função dá para reutilizar o código

# exemplo
def saudacao(nome):
   print(f"Olá, {nome}")

print("\n Chamando a função saudação:")
saudacao("Alice")
saudacao("Bruno")

# FUNÇÃO COM RETORNO: funções que receben informaçoes e  retornam informações
def quadrado(numero):
   resultado = numero ** 2
   return resultado

print("\n Chamando função quadrado:")
resultado_quadrado = quadrado(8)
print("Resultado função quadrado:", resultado_quadrado)

# função com multiplos parâmetros
# def soma(n1, n2):
#    resultado = n1 + n2
#    return resultado
# resultado_soma = soma(20,50)
# print("\n Resultado da soma de n1 + n2=", resultado_soma)

def soma(n1, n2):
   resultado = n1 + n2
   return resultado
n1 = 25
n2 = 30
resultado_soma = soma(n1,n2)
print(f"Resultado da soma de {n1} + {n2} = {resultado_soma}")