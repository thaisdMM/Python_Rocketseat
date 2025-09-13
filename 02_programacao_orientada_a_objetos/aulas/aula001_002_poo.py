# Classe exemplo
class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    # método
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."


# Objetos
pessoa1 = Pessoa("Marcos", 55)
print(f"Nome {pessoa1.nome}")
print(f"Idade: {pessoa1.idade}")
# depois da criação de saudação
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = Pessoa("Tânia", 60)
mensagem2 = pessoa2.saudacao()
print(mensagem2)
