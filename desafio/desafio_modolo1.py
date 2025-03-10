def adiciona_contato(lista_contatos, nome_contato, telefone_contato, email_contato):
   contato = {"nome": nome_contato,"telefone": telefone_contato, "email": email_contato, "favorito": False}

   if not nome_contato or nome_contato == " ":
      print("\nO nome do contato nao pode ser vazio!")
   else:
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
   indice_contato_ajustado = (int(indice_contato) -1)
   if indice_contato_ajustado < 0 or indice_contato_ajustado >=len(lista_contatos):
      print("\nNúmero de contato inválido ou não existe.")
      print("PAROU NO IF")
      return
   
   print("parou depois do retur 1")
   if not novo_contato or novo_contato == " ":
      print("\nO nome do novo contato não pode ser vazio!")
      print("parou antes do segundo return")
      return
   
   print( "parou depoi do segundo return")

   lista_contatos[indice_contato_ajustado] ["nome"] = novo_contato
   lista_contatos[indice_contato_ajustado] ["telefone"] = novo_telefone_contato
   lista_contatos[indice_contato_ajustado] ["email"] = novo_email_contato
   print(f"\nO contato {indice_contato} foi atualizado para {novo_contato} com sucesso!")
      
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
   
   escolha = input("Digite sua escolha: ").strip() # para não contar espaços vazios no início e no final

   if escolha == "1":
      nome_contato = input("\nDigite o nome do contato: ").strip()
      telefone_contato = input("Digite o telefone do contato: ").strip()
      email_contato = input("Digite o e-mail do contato: ").strip()
      adiciona_contato(lista_contatos, nome_contato, telefone_contato, email_contato)

   elif escolha == "2":
      ver_contatos(lista_contatos)
   
   elif escolha == "3":
      ver_contatos(lista_contatos)
      
      indice_contato = int(input("\nDigite o número do indice do contato que deseja atualizar: "))
      if indice_contato < 0 or indice_contato >= len(lista_contatos):
         print("\nNúmero de contato inválido ou não existe.")
      
      else: 
         novo_contato = input("Digite o novo nome do contato: ").strip()
         novo_telefone_contato = input("Digite o novo telefone do contato: ").strip()
         novo_email_contato = input("Digite o novo email do contato: ").strip()
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