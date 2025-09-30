# Módulo padrão

print("Exemplo de importação de módulo padrão com o import")
# o importe importa o módulo todo - não é boa pratica
import math #para operações matemáticas

raiz_quadrada = math.sqrt(25)
print(f"A raiz quadradada de 25 é {raiz_quadrada}")

print("Exemplo de importação de módulo padrão com o from modulo import:")
# o importe importa algo do módulo - é boa pratica, pois importa só que precisa
from math import sqrt
raiz_quadrada2 = sqrt(81)
print(f"A raiz quadrada de 81 é: {raiz_quadrada2}")

# Modulo personalizado
# Esse meu_modulo nós criamos um novo arquivo, criamos as funções dentro do módulo e importamos ele
print("Exemplo de criação e utilização de um módulo personalizado")

# PODE SER ASSIM OU COMO ESTÁ ABAIXO
# import meu_modulo

# mensagem = meu_modulo.saudacao("Thaís")
# resultado_dobro = meu_modulo.dobro(6)
# print(mensagem)
# print(f"O dobro de 6 é {resultado_dobro}")

from meu_modulo import saudacao, dobro

mensagem = saudacao("Moreira")
resultado_dobro = dobro(5)
print(mensagem)
print(f"O dobro de 5 é {resultado_dobro}")