# Composição 
# uma classe Carro que possui um objeto de composição chamado Motor. O motor é uma parte essencial do carro.

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

class Carro:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

# Criando um carro com composição
motor_carro = Motor("Gasolina")
meu_carro = Carro("Ford", "Focus", motor_carro)

print(f"Marca: {meu_carro.marca}, Modelo: {meu_carro.modelo}, Motor: {meu_carro.motor.tipo}")


# Associação
# duas classes, Pessoa e Endereco, que estão associadas. Uma pessoa tem um endereço, mas o endereço não é uma parte essencial da pessoa.
class Endereco:
    def __init__(self, rua, cidade):
        self.rua = rua
        self.cidade = cidade

class Pessoa:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

# Criando objetos associados
endereco1 = Endereco("123 Main St", "Cidade A")
pessoa1 = Pessoa("João", endereco1)

print(f"{pessoa1.nome} mora em {pessoa1.endereco.rua}, {pessoa1.endereco.cidade}")


# Herança 
# herança para criar subclasses Cachorro e Gato que herdam da classe base Animal.

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

dog = Cachorro("Rex")
cat = Gato("bolinha-de-pelo")

print(f"{dog.nome} faz: {dog.fazer_som()}")
print(f"{cat.nome} faz: {cat.fazer_som()}")



# Agregação
# uma classe Departamento que pode conter vários objetos Professor. 
# Os professores são agregados ao departamento, mas podem existir independentemente.

class Professor:
    def __init__(self, nome):
        self.nome = nome

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    def adicionar_professor(self, professor):
        self.professores.append(professor)

# Criando objetos de agregação
professor1 = Professor("Fabio")
professor2 = Professor("Diogo")
departamento = Departamento("Departamento de Ciência da Computação")
departamento.adicionar_professor(professor1)
departamento.adicionar_professor(professor2)

for professor in departamento.professores:
    print(f"Professor do departamento {departamento.nome}: {professor.nome}")


