# Classe base Veiculo
class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f"{self.marca} {self.modelo} está acelerando.")

    def frear(self):
        print(f"{self.marca} {self.modelo} está freando.")

# Subclasse Carro que herda de Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self.num_portas = num_portas

    def acelerar(self):
        print(f"Carro {self.marca} {self.modelo} está acelerando com {self.num_portas} portas.")

# Subclasse Moto que herda de Veiculo
class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindradas):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def acelerar(self):
        print(f"Moto {self.marca} {self.modelo} está acelerando com {self.cilindradas} cilindradas.")