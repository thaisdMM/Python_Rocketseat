# while - Enquanto o usuário nao digitar a opção de sair ele continua rodando
   
def adicionar_tarefa(tarefas, nome_tarefa):
   
   # chave: tarefa: nome da tarefa 
   # chave completada: indicar se essa tarefa já foi completada ou não(4,5 do menu)
   # Como temos 1 ou mais informações vamos usar o dict
   tarefa = {"tarefa": nome_tarefa, "completada": False} #como está inserindo, em primeiro momento completada é sempre False
   tarefas.append(tarefa)
   # tarefas.append({"tarefa": "nome_tarefa", "completada": False}) > mesmo código acima
   print(f"\nA tarefa {nome_tarefa} foi adicionada com sucesso!")
   return

def ver_tarefas(tarefas):
   print("\n Lista de tarefas: ")
   for indice, tarefa in enumerate(tarefas, start=1): #start=1 para contar do 1 e nao do 0 como de praxe em listas
      status = "✓" if tarefa["completada"] else " "
      nome_tarefa = tarefa["tarefa"]
      print(f"{indice}. [{status}] : {nome_tarefa}")
   return

def atualizar_nome_tarefas(tarefas, indice_tarefa, novo_nome_tarefa):
   indice_tarefa_ajustado = int(indice_tarefa) -1 #porque com o start=1 começa no 1, mas na verdade a tarefa começa com 0 - dá erro se nao converter para int
   #esse if abaixo é para tratar casos os numeros digitados das tarefas sao maiores ou menores que os existentes
   if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado <len(tarefas):
      tarefas[indice_tarefa_ajustado] ["tarefa"] = novo_nome_tarefa
      print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa} com sucesso!")
   else:
      print("Índice de tarefa inválido.")
   return

def completar_tarefa(tarefas, indice_tarefa):
   indice_tarefa_ajustado = int(indice_tarefa) -1
   if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado <len(tarefas):
      tarefas[indice_tarefa_ajustado] ["completada"] = True
      print(f"Tarefa {indice_tarefa} marcada como completada com sucesso!")
   else:
      print("Índice de tarefa inválido.")
   return

def deletar_tarefa_completadas(tarefas): 
   for tarefa in tarefas:
      if tarefa["completada"]:
         tarefas.remove(tarefa)
   print("Tarefas completadas foram deletadas.")
   return

tarefas = []   

while True:

   print("\nMenu do Gerenciador de Lista de tarefas:")
   print("1. Adicionar tarefa")
   print("2. Ver tarefas")
   print("3. Atualizar tarefa")
   print("4. Completar tarefa")
   print("5. Deletar tarefas completadas")
   print("6. Sair")

   escolha = input("Digite a sua escolha:")

   if escolha == "1":
      nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
      adicionar_tarefa(tarefas, nome_tarefa)
   
   elif escolha == "2":
      ver_tarefas(tarefas)

   elif escolha == "3":
      ver_tarefas(tarefas)
      indice_tarefas = input("Digite o número do índice da tarefa que deseja atualizar: ")
      novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
      atualizar_nome_tarefas(tarefas, indice_tarefas, novo_nome_tarefa)
   
   elif escolha == "4":
      ver_tarefas(tarefas)
      indice_tarefa = input("Digite o número do índice da tarefa que deseja completar: ")
      completar_tarefa(tarefas, indice_tarefa)

   elif escolha == "5":
      deletar_tarefa_completadas(tarefas)
      ver_tarefas(tarefas)

   elif  escolha == "6":
      break
      
print("Programa finalizado")