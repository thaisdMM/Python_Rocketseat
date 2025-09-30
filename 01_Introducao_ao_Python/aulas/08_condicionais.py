# tomar decições com base em condições que executam um bloco no python

# if, elif, else

# if

# idade = 19
# print("Exemplo de comando if")
# # >=
# if idade >= 18:
#    print("Você é maior de idade") #tem que dar um tab para que execute o bloco de código

# # ==
# if idade == 19:
#    print("Você tem 19 anos")

# # <
# if idade <18:
#    print("Você tem 19 anos")

# # !=
# if idade != 10:
#    print("Você nao tem 10 anos.")

idade = 18
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