#SOLID (S) - Responsabilidade Única

class SistemaCadastral:

    def cadastrar(self, nome:str, idade:int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazena_usuario(nome, idade)
        else:
            self.__erro

    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False
        
    def __armazena_usuario(self, nome: str, idade: int) -> None:
        print('acessando o banco de dados')
        print(f'cadastrar o usuario {nome}, idade {idade}')

    def __erro(self) -> None:
        print('dados inválidos')
