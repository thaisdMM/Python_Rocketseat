# WHILE > lOOPING> uma estrutura que permite repertir um bloco de codigo enquanto(while) uma condição for verdadeira

print("Exemplo de while")
contador = 0
while contador < 5:
   print("Contagem:", contador)
   contador += 1
   # contador = contador +1
   #contador -= 1 aqui vai decrementar

print("programa finalizado")

# para nao entra no looping usar o break

print("Exemplo de while com o break")
contador = 0
# while contador < 5:
while True:
   print("Contagem:", contador)
   contador += 1
   # contador = contador +1
   #contador -= 1 aqui vai decrementar
   if contador == 5:
      break 

print("programa finalizado")

