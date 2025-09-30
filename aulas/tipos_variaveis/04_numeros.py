# Inteiro - int

numero_inteiro = 4
print ("Inteiro =", numero_inteiro)

# Real com ponto flutuante - float

numero_real = 3.14
print("Real com ponto flutuante = ", numero_real)

#type() função que retorna o tipo da variavel

print("Tipo da variável inteiro: ",type(numero_inteiro))
print("Tipo da variável Real", type(numero_real))

#OPERAÇÕES ARITIMÉTICAS

# Soma +

soma = 1+1
print("1+1 =", soma)

# Subtração

subtracao = 1-1
print("1-1 =", subtracao)

# multiplicação

multiplicacao = 2*2
print("2*2 =", multiplicacao)

# divisao

divisao = 5/2
print("5/2 =", divisao)
#a divisao tem resultado float
print("Tipo da variável resultado da divisão =", type(divisao)) 
#convertendo float para int
print("Convertando float para int: ", int(divisao))

#float
print("Convertendo o resultado da soma de int para float: ", float(soma))

# modulo % é o restantante da divisao
modulo = 5%2
print("modulo =", modulo)

#para a divisao nao ter resultado float tem que usar //

divisao = 5//2
print("5//2 =", divisao)
#// faz o resultado ficar inteiro
print("Tipo da variável resultado da divisão =", type(divisao)) 
#convertendo  int para float
print("Convertando int para float: ", float(divisao))
