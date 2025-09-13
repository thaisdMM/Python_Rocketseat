# Herança e Polimorfismo

print("\nExemplo de herança:")


class Animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou.")

    def emitir_som(self):
        pass


class Cachorro(Animal):
    # Polimofismo - mesmo método de uma classe mãe, mas com implementação/comportamento diferente
    def emitir_som(self):
        return "Au au"


class Gato(Animal):
    # Polimofismo - mesmo método de uma classe mãe, mas com implementação/comportamento diferente
    def emitir_som(self):
        return "Miau!"


dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")
dog.andar()


print("\nExemplo de Polimorfismo:")
animais = [dog, cat]
for animal in animais:
    print(f"{animal.nome} faz {animal.emitir_som()}")
