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
   contato = {"nome": nome_contato,"telefone": telefone_contato, "email": email_contato, "favorito": False}

   lista_contatos.append(contato)
   print(f"\nO contato {nome_contato} foi adicionado a agenda com sucesso!")
   return

def ver_contatos(lista_contatos):
   print("\n Lista de contatos: ")
   for indice, contato in enumerate(lista_contatos, start=1):
      status = "★" if contato["favorito"] else " "
      nome_contato = contato["nome"]
      telefone_contato = contato["telefone"]
      email_contato = contato["email"]
      print(f"{indice}. [{status}] : {nome_contato}, {telefone_contato}, {email_contato} ")
   return

def editar_contato(lista_contatos, indice_contato, novo_contato, novo_telefone_contato, novo_email_contato):
   indice_contato_ajustado = int(indice_contato) -1
   if indice_contato_ajustado >= 0 and indice_contato_ajustado <len(lista_contatos):
      lista_contatos[indice_contato_ajustado] ["nome"] = novo_contato
      lista_contatos[indice_contato_ajustado] ["telefone"] = novo_telefone_contato
      lista_contatos[indice_contato_ajustado] ["email"] = novo_email_contato
      print(f"\nO contato {indice_contato} foi atualizado para {novo_contato} com sucesso!")
   else:
      print("\nNúmero de contato inválido ou não existe.")
   return

#melhoria: nao permirtir marcar novamente um contato que já está marcado como favorito
def marcar_contato_favorito(lista_contatos, indice_contato):
   indice_contato_ajustado = int(indice_contato) -1
   if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(lista_contatos):
      lista_contatos[indice_contato_ajustado] ["favorito"] = True
      print(f"\nO contato {indice_contato} foi marcado como favorito!")
   else:
      print("\nNúmero de contato inválido ou não existe.")
   return

def ver_contatos_favoritos(lista_contatos):
   print("\nLista de contatos favoritos: ")
   tem_favoritos = False
   for indice, contato in enumerate(lista_contatos, start=1):      
      if contato ["favorito"]: 
         tem_favoritos = True
         print(f"{indice}. ★ : {contato['nome']}, {contato['telefone']}, {contato['email']}")
   
   if not tem_favoritos:
      print("Não há contatos marcados como favoritos.")
   return

def desmarcar_contato_favorito(lista_contatos, indice_contato):
   indice_contato_ajustado = int(indice_contato) - 1
   if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(lista_contatos):
         lista_contatos[indice_contato_ajustado] ["favorito"] = False
         print(f"O contato {indice_contato} foi desmarcado como favorito!")   
   else:
      print("Número de contato inválido ou nao exite.")         
   return

def apagar_contato(lista_contatos, indice_contato):
   indice_contato_ajustado = int(indice_contato) -1
   if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(lista_contatos):
      for contato in lista_contatos:
         if indice_contato:
            lista_contatos.remove(contato)
            print(f"O contato {indice_contato} foi apagado com sucesso!")

   else:
      print("Número do contato iválido ou não existe.")
   return

lista_contatos = []

while True:
   print("\nMenu do app Agenda:")
   print("\n1. Adicionar um contato.")
   print("2. Visualizar a lista de contatos.")
   print("3. Editar um contato da lista de contatos.")
   print("4. Marcar um contato como favorito.")      
   print("5. Ver a lista de contatos favoritos.")
   print("6. Desmarcar um contato na lista de favoritos.")
   print("7. Apagar um contato da lista de contatos.")
   print("8. Sair da agenda.\n")
   
   escolha = input("Digite sua escolha: ")

   if escolha == "1":
      nome_contato = input("\nDigite o nome do contato: ")
      telefone_contato = input("Digite o telefone do contato: ")
      email_contato = input("Digite o e-mail do contato: ")
      adiciona_contato(lista_contatos, nome_contato, telefone_contato, email_contato)

   elif escolha == "2":
      ver_contatos(lista_contatos)
   
   elif escolha == "3":
      ver_contatos(lista_contatos)
      indice_contato = input("\nDigite o número do indice do contato que deseja atualizar: ")
      novo_contato = input("Digite o novo nome do contato: ")
      novo_telefone_contato = input("Digite o novo telefone do contato: ")
      novo_email_contato = input("Digite o novo email do contato: ")
      editar_contato(lista_contatos, indice_contato, novo_contato, novo_telefone_contato, novo_email_contato)

   elif escolha == "4":
      ver_contatos(lista_contatos)
      indice_contato = input("\nDigite o número do indice do contato que deseja marcar como favorito: ")
      marcar_contato_favorito(lista_contatos, indice_contato)

   elif escolha == "5":
      ver_contatos_favoritos(lista_contatos)
   
   #nao deixar marcar quando a lista está vazia
   elif escolha == "6":
      ver_contatos_favoritos(lista_contatos)
      indice_contato = input("\nDigite o número do contato favorito que você deseja desmarcar: ")
      desmarcar_contato_favorito(lista_contatos, indice_contato)
      ver_contatos_favoritos(lista_contatos)

   elif escolha == "7":
      ver_contatos(lista_contatos)
      indice_contato = input("Digite o número do contato que deseja apagar: ")
      apagar_contato(lista_contatos, indice_contato)

   elif escolha == "8":
      break

print("\nPrograma finalizado!")