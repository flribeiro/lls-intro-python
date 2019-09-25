class Funcionário:


    def __init__(self, nome, salário, cpf):
        self.nome = nome
        self.salário = salário
        self.cpf = cpf


    def get_bonificação(self):
        with open('comissão.txt', 'w', encoding='utf-8') as info:
            info.write(f'O {self.nome} obteve uma comissão de '
                       f'R${self.salário * 0.20:.2f}')
        return 'Seu cálculo está disponível no arquivo: "comissões.txt"'


class Gerente(Funcionário):
    pass


    # Polimorfismo: Sobreescrita de método
    def get_bonificação(self):
        return self.salário * 0.10 + 1000.00
        # Para não ficar alterando sempre que mudar no Funcionário:
        # return super().get_bonificação() + 1000.00


# Instância
f = Funcionário('Carlinhos', 1500.00, '41287963152')
g = Gerente('Marquinhos', 3000.00, '96874259633')
# Chamada de método
print(f.get_bonificação())
print(g.get_bonificação())
