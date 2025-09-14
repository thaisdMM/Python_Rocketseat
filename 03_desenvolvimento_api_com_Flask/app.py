from flask import Flask

app = Flask(__name__)


# definindo a rota / é a padrão
@app.route("/")
def hello_world():
    return "Hello World"


@app.route("/about")
def about():
    return "Pagina sobre"


# modo de desenvolvimento local
if __name__ == "__main__":
    # debug permite ver informações para ver o que está acontecendo no servidor web
    app.run(debug=True)
