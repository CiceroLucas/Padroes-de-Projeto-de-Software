# Classe base Animal
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

# Subclasse Cachorro que herda de Animal
class Cachorro(Animal):
    def fazer_som(self):
        return f"{self.nome} faz 'Au Au!'"

# Subclasse Gato que herda de Animal
class Gato(Animal):
    def fazer_som(self):
        return f"{self.nome} faz 'Miau!'"

# Função que demonstra o polimorfismo
def fazer_barulho(animal):
    return animal.fazer_som()

# Criando instâncias das classes
rex = Cachorro("Rex")
whiskers = Gato("Whiskers")

# Chamando a função usando polimorfismo
print(fazer_barulho(rex))        # O resultado depende do tipo de animal
print(fazer_barulho(whiskers))   # O resultado depende do tipo de animal