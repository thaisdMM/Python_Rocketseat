from flask import Flask, request
from models.task import Task

app = Flask(__name__)


# CRUD
# CREATE, READ, UPDATE, DELETE
# Tabela: tarefa

# sem banco de dados, vamos começar com essa lista para organizar os dados(tasks)
tasks = []


# Create - Olha a criação da tarefa no arquivo da aula no https://editor.swagger.io/
@app.route("/tasks", methods=["POST"])
def create_task():
    # receber os dados do cliente
    data = request.get_json()
    print(data)
    return "Test"


# modo de desenvolvimento local
if __name__ == "__main__":
    # debug permite ver informações para ver o que está acontecendo no servidor web
    app.run(debug=True)
