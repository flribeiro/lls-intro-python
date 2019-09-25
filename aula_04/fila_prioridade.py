import heapq

class FilaDePrioridade:


    def __init__(self):
        # A fila será uma lista vazia, para ser incrementada posteriormente com
        # valores
        self.fila = []
        # O índice será a posição que ocupará na lista
        self.índice = 0


    def inserir(self, item, prioridade):
        # Insere item em uma lista
        # -prioridade é negado para fazer a lista ordenar da mais alta para a
        # mais baixa prioridade
        heapq.heappush(self.fila, (-prioridade, self.índice, item))


    def remover(self):
        # Retorna o menor item, é a chave para fazer com que os menores itens
        # sumam da lista
        return heapq.heappop(self.fila)[-1]


class Item:


    def __init__(self, nome):
        self.nome = nome


    def __repr__(self):
        return self.nome


# Instância (pegar a classe e criar um objeto a partir dela) da classe FilaDePrioridade
fila = FilaDePrioridade()
# Analogia: Fila de transplante, os mais velhos tem mais preferência
# Fazemos a chamada do método
fila.inserir(Item('Marcos'), 28)
fila.inserir(Item('João'), 30)
fila.inserir(Item('Maria'), 18)

print(fila.remover())
