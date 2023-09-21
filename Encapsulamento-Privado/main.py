from pessoa import Pessoa
from cidade import Cidade

lucas = Pessoa('Lucas', 22, '091232833-28')
lucas.beber('cerveja')
lucas.beber('coca-cola')

cajazeiras = Cidade("Cajazeiras", "Paraíba")

# Acessando os atributos encapsulados por meio dos métodos getters
print(cajazeiras.nome)
print(cajazeiras.estado)

cajazeiras.apresentar()
