class Personagem:
    def __init__(self, name: str) -> None:
        self.name = name

    def print_name(self) -> str:
        print(self.name)

personagem = Personagem('Zed')
personagem.print_name()