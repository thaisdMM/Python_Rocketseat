# Entradada de dados - input

# Erro de comparação str com int
# idade = input("Quantos anos você tem?")
# TypeError: '>=' not supported between instances of 'str' and 'int'

# converte str em int
idade = int(input("Quantos anos você tem?"))
print("Exemplo de if elif else:")
if idade >=18:
   print("Você é maior de idade")
elif idade >=12:
   print("Você é adolescente")
else:
   print("Você é menor de idade")

#construindo if e else em 1 linha:
mensagem = "Pode tirar a carteira de habilitação" if idade >= 18 else "Você não pode tirar a carteira de habilitação"
print(mensagem)