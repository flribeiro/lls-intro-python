class Fila():

    __quantidade = 0

    def __init__(self):
        """Método construtor da classe Fila."""
        self.fila = list()
        self.incrementa()

    def inserir(self, obj):
        """Insere um objeto na fila."""
        self.fila.append(obj)

    def remover(self):
        """Remove um objeto da fila, mostra qual foi o objeto removido e
        mostra a situação da fila após a operação."""
        saindo = self.fila.pop(0)
        print(f'Tirando {saindo} da fila.')
        print(f'Situação atual da fila:\n{self.fila}')

    def __del__(self):
        """Elimina a instância da classe."""
        print("Instância deletada")
        self.decrementa()

    def __str__(self):
        """Retorna uma descrição da instância."""
        return f'Situação atual da fila:\n{self.fila}'

    @classmethod
    def contador(cls):
        """Método de classe que mostra a quantidade de instâncias existentes."""
        print(cls.__quantidade)

    @classmethod
    def incrementa(cls):
        """Método de classe que é chamado para incrementar a quantidade de
        instâncias."""
        cls.__quantidade += 1
        print(cls.__quantidade)

    @classmethod
    def decrementa(cls):
        """Método de classe que é chamado para decrementar a quantidade de
        instâncias."""
        cls.__quantidade -= 1
        print(cls.__quantidade)

    @staticmethod
    def testa_classe():
        """Método estático, apenas para fins de demonstração."""
        print("Classe testada com sucesso.")

