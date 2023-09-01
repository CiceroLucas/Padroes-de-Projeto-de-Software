class Coxinha:

    def __init__(self):
        """
        O construtor __init__ recebe um objeto e constroi aquele como uma instância da classe coxinha.
        self => objeto que recebe atribuições de aspecto e composição.
        """

        self.aspecto = 'fast food delicioso'
        self.composicao = 'massa frita e recheio'
        print('Uma nova coxinha foi criada')

    def info(self):
        """
        O método info recebe um objeto de sua classe e informa seus atributos base.
        self => Tem de ser um objeto da classe coxinha que utiliza do método info.
        """

        print(f'Toda coxinha tem um aspecto de {self.aspecto} e é feita de {self.composicao}')

coxinha_de_batata_doce = Coxinha()
coxinha_de_batata_doce.info()