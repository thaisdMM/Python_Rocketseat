# ### Sobre o desafio

# Nesse desafio desenvolveremos uma agenda para salvar, editar, deletar e marcar um contato como favorito. O resultado da aplicação deve ser apresentado no terminal, assim como foi visto no módulo “Introdução ao Python”.
# ### Regras da aplicação

# A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.

# Deve ser possível adicionar um contato 
#> tem que poder ser vazio acho que tinha um codigo=

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

def adiciona_contato(lista_contatos, nome_contato, telefone_contato, email_contato):
   novo_contato = {"nome": nome_contato,"telefone": telefone_contato, "email": email_contato, "favorito": False}

   lista_contatos.append(novo_contato)
   print(f"\nO novo contato {nome_contato} adicionado a agenda com sucesso!")
   return

def ver_contatos(lista_contatos):
   print("\n Lista de contatos: ")
   for indice, novo_contato in enumerate(lista_contatos, start=1):
      status = "★" if novo_contato["favorito"] else " "
      nome_contato = novo_contato["nome"]
      telefone_contato = novo_contato["telefone"]
      email_contato = novo_contato["email"]
      print(f"{indice}. [{status}] : {nome_contato}, {telefone_contato}, {email_contato} ")
   return

def editar_contato(lista_contatos):
   return


lista_contatos = []

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

   if escolha == "1":
      nome_contato = input("Digite o nome do novo contato: ")
      telefone_contato = input("Digite o telefone do novo contato: ")
      email_contato = input("Digite o e-mail do novo contato: ")
      adiciona_contato(lista_contatos, nome_contato, telefone_contato, email_contato)

   if escolha == "2":
      ver_contatos(lista_contatos)
   
   if escolha =="3":
      editar_contato(lista_contatos)

   elif escolha == "8":
      break

print("\nPrograma finalizado!")