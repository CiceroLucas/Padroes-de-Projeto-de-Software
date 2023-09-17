class Teste():
    def __init__(self,valor):
        self.x = valor
        
    def get_valor(self):
        # Método getter para retornar o valor do atributo x:
        return self.x
    
    def set_valor(self, valor):
        # Método settter para atribuir um novo valor a o atributo x
        self.x = valor
        
teste = Teste(10)
print('Valor do objeto: ', teste.get_valor())

val = int(input('Digite um valor inteiro: '))
teste.set_valor(val)
print('Valor do objeto após a atribuição: ', teste.get_valor())