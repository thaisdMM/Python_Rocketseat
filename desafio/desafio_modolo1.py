# ### Sobre o desafio

# Nesse desafio desenvolveremos uma agenda para salvar, editar, deletar e marcar um contato como favorito. O resultado da aplicação deve ser apresentado no terminal, assim como foi visto no módulo “Introdução ao Python”.
# ### Regras da aplicação

# A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.

# Deve ser possível adicionar um contato

# O contato pode ter os dados: é um dict

# Nome

# Telefone

# Email

# Favorito (está opção é para poder marcar um contato como favorito)

# Deve ser possível visualizar a lista de contatos cadastrados

# Deve ser possível editar um contato

# Deve ser possível marcar/desmarcar um contato como favorito

# Deve ser possível ver uma lista de contatos favoritos

# Deve ser possível apagar um contato



litas_contatos = []

while True:
   print("\nMenu do app Agenda:")
   print("\n1. Adicionar um contato.")
   print("2. Visualizar a lista de contatos.")
   print("3. Editar um contato da lista de contatos.")
   print("4. Ver a lista de contatos favoritos.")
   print("5. Marcar um contato como favorito.")
   print("6. Desmarcar um contato na lista de favoritos.")
   print("7. Apagar um contato da lista de contatos.")
   print("8. Sair da agenda.\n")
   
   escolha = input("Digite sua escolha: ")

   if escolha == "8":
      break

print("Programa finalizado!")