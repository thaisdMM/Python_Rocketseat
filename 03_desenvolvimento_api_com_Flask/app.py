from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)


# CRUD
# CREATE, READ, UPDATE, DELETE
# Tabela: tarefa

# sem banco de dados, vamos começar com essa lista para organizar os dados(tasks)
tasks = []

task_id_control = 1


# Create - Olha a criação da tarefa no arquivo da aula no https://editor.swagger.io/
@app.route("/tasks", methods=["POST"])
def create_task():
    # global para pegar a variavel global fora da função
    global task_id_control
    # receber os dados do cliente
    data = request.get_json()
    # new_task = Task(title=data['title']) # pode ser assim também, para esse caso
    # "description", "" -> vazia, assim se o cliente não enviar a description ainda assim, dá para criar a task
    new_task = Task(
        id=task_id_control,
        title=data.get("title"),
        description=data.get("description", ""),
    )
    # toda vez que criar uma nova task, cria um identificador unico
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso"})


# modo de desenvolvimento local
if __name__ == "__main__":
    # debug permite ver informações para ver o que está acontecendo no servidor web
    app.run(debug=True)
