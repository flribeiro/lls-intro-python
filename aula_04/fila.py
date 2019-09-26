
class Fila():


    quantidade = 0

    def __init__(self):
        self.__fila = list()
        self.incrementa()

    def inserir(self, obj):
        self.fila.append(obj)

    def remover(self):
        self.fila.pop(0)

    @classmethod
    def contador(cls):
        print(cls.quantidade)
        print(cls.__repr__)

    @classmethod
    def incrementa(cls):
        cls.quantidade += 1
        print(cls.quantidade)
        print(cls.__repr__)

    @staticmethod
    def testa_classe():
        print("Classe testada com sucesso.")