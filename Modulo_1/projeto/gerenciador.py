# while - Enquanto o usuário nao digitar a opção de sair ele continua rodando

while True:

   print("\nMenu do Gerenciador de Lista de tarefas:")
   print("1. Adicionar tarefa")
   print("2. Ver tarefas")
   print("3. Atualizar tarefa")
   print("4. Completar tarefa")
   print("5. Deletar tarefa")
   print("6. Sair")

   escolha = input("Digite a sua escolha:")
   if  escolha == "6":
      break
      
print("Programa finalizado")