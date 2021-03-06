"""Primeira parte do exercício/desafio:

Termine de implementar a classe abaixo. A classe pessoa deverá ter os
seguintes atributos:
    - nome
    - idade
    - peso 
    - altura

Vocè também deverá implementar os seguintes métodos:
    - envelhecer(): não recebe nenhum parâmetro, a pessoa envelhece 1 ano 
        cada vez que o método é invocado. Se a pessoa tiver até 21 anos, ela 
        deve crescer 0,5 cm. a cada aniversário. Deve retornar a nova idade.
    - engordar(): recebe como parâmetro o pesso em Kg que a pessoa está 
        engordando. Deve retornar o novo peso.
    - emagrecer(): recebe como parâmetro o peso em Kg que a pessoa está 
        emagrecendo. Deve retornar o novo peso.
    - crescer(): recebe como parâmetro a medida de crescimento em centímetros.
        Retorna a nova altura em metros.
    - __str__(): sobrescrever o método __str__ do Python de forma que seja 
        retornado uma ficha da pessoa com todas as informações: nome, idade,
        peso e altura.

Atenção para os tipos das variáveis que irão armazenar os atributos. 
Lembre-se que o primeiro argumento de todos os métodos deve ser o self 
    (referência à própria instância).
"""

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade <= 21:
            self.crescer(0.5)
        return self.idade
    
    def engordar(self, peso_mais):
        self.peso += peso_mais
        return self.peso
    
    def emagrecer(self, peso_menos):
        self.peso -= peso_menos
        return self.peso

    def crescer(self, cm):
        self.altura += (cm / 100)
        return self.altura

    def __str__(self):
        pessoa = f"""Nome: {self.nome}
Idade: {self.idade} anos
Peso: {self.peso} Kg.
Altura: {self.altura:.3f} m."""
        return pessoa