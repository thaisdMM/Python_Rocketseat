from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)


# CRUD
# CREATE, READ, UPDATE, DELETE
# Tabela: tarefa

# sem banco de dados, vamos começar com essa lista para organizar os dados(tasks)
tasks = []

task_id_control = 1


# CREATE - Olha a criação da tarefa no arquivo da aula no https://editor.swagger.io/
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


# READ - ver a listagem das tarefas GET no arquivo da aula no https://editor.swagger.io/
# retorna objetos de Task, por isso depois tem que usar o to_dict
@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    # Pode ser feito o get da task do modo abaixo também
    # task_liste[]
    #  for task in tasks:
    #     task_list.append(task.to_dict())
    outptut = {"tasks": task_list, "total_tasks": len(task_list)}
    return jsonify(outptut)


# parametro de rota id -> <int:id>
@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    # task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404


# # parâmetros de rota - teste para aprendizado: -> variavel entre <>
# @app.route("/user/<int:username_id>")
# def show_user(username_id):
#     print(username_id)
#     # #retorna uma str(default), se quiser retornar outro valor tem que converter ao passar a variavel
#     print(type(username_id))
#     return f"{username_id}"


# modo de desenvolvimento local
if __name__ == "__main__":
    # debug permite ver informações para ver o que está acontecendo no servidor web
    app.run(debug=True)
