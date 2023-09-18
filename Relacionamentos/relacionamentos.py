# Associação
class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

class Endereco:
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade

endereco1 = Endereco("123 Main St", "Cidade A")
pessoa1 = Pessoa("João", endereco1)

print(f"{pessoa1.nome} mora em {pessoa1.endereco.rua}, {pessoa1.endereco.cidade}")

# Herança 
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

dog = Cachorro("Fido")
cat = Gato("Whiskers")

print(f"{dog.nome} faz: {dog.fazer_som()}")
print(f"{cat.nome} faz: {cat.fazer_som()}")


# Agregação
class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

class Aluno:
    def __init__(self, nome):
        self.nome = nome

aluno1 = Aluno("Alice")
aluno2 = Aluno("Bob")

curso = Curso("Python 101")
curso.adicionar_aluno(aluno1)
curso.adicionar_aluno(aluno2)

for aluno in curso.alunos:
    print(f"Aluno do curso {curso.nome}: {aluno.nome}")

