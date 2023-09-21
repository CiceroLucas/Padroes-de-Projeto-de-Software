# Variáveis e atribuição:

nome = "Alice"
idade = 30
salario = 2500.50

# Valor nulo (null)
# Em Python, None equivale ao valor nulo (null).
reais = None

"""
Operadores Matemáticos:
soma = 5 + 3
subtracao = 10 - 4
multiplicacao = 2 * 6
divisao = 8 / 2
resto = 9 % 4
exponenciação = 10 ** 2
"""

# Saídas
print("Welcome to Python!")

string_1 = "Camaleão"
string_2 = "plano"
print("contei que o %s. 'não tinha %s." % (string_1, string_2))


# Entradas
nome = input(" qual o seu nome ? ")
print("olá", nome)

# Estruturas Condicionais (if-elif-else):
idade = 25
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


# Estruturas de Repetição (for):
for i in range(5):
    print("Número:", i)


# Funções:
def saudacao(nome):
    return "Olá, " + nome + "!"


mensagem = saudacao("João")
print(mensagem)


# Listas
frutas = ["maçã", "banana", "laranja"]
print("Primeira fruta:", frutas[0])
print("Número de frutas:", len(frutas))

# Dicionários
pessoa = {"nome": "Alice", "idade": 35}
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
