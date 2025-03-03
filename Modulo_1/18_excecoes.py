
print("Exemplo de captura excções")
try:
  numero = int(input("Digite um número inteiro:"))
  resultado = 10 / numero
except ValueError as e:
  print(f"Erro de value error: {e}")
  raise ValueError("Tipo de variaveis incompativeis") #você pode levantar o erro
except Exception as e:
  print(f"Erro: {e}")
# o else vai ser executado só se der certo
else:
  print(f"Resultado: {resultado}")
# o finaly permite que vc execute mesmo se deu certo ou errado
finally:
  print("Operação finalizada")