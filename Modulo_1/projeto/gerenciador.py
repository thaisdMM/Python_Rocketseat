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
   for indice, tarefa in enumerate(tarefas):
      status = "✓" if tarefa["completada"] else " "
      nome_tarefa = tarefa["tarefa"]
      print(f"{indice}. [{status}] : {nome_tarefa}")

tarefas = []   

while True:

   print("\nMenu do Gerenciador de Lista de tarefas:")
   print("1. Adicionar tarefa")
   print("2. Ver tarefas")
   print("3. Atualizar tarefa")
   print("4. Completar tarefa")
   print("5. Deletar tarefa")
   print("6. Sair")

   escolha = input("Digite a sua escolha:")

   if escolha == "1":
      nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
      adicionar_tarefa(tarefas, nome_tarefa)
   
   elif escolha == "2":
      ver_tarefas(tarefas)




   elif  escolha == "6":
      break
      
print("Programa finalizado")

