def moeda(moeda):
    return f'R${moeda:.2f}'.replace('.', ',')


def leiaDinheiro(moeda):
    while True:
        moeda = str(input('Digite o preço: R$')).replace(',', '.')
        if moeda.isalpha():
            print(f'ERRO: "{moeda}" é um preço inválido!')
        elif moeda.strip() in '':
            print(f'ERRO: "" é um preço inválido!')
        # isnumeric: int
        # isprintable: str com pontos
        elif moeda.isnumeric() or moeda.isprintable():
            return float(moeda)


def metade(moeda, show=False):
    moeda /= 2
    if show:
        return f'R${moeda:.2f}'.replace('.', ',')
    else:
        return moeda


def dobro(moeda, show=False):
    moeda *= 2
    if show:
        return f'R${moeda:.2f}'.replace('.', ',')
    else:
        return moeda


def aumentar(moeda, desconto=10, show=False):
    moeda += (moeda * desconto) / 100
    if show:
        return f'R${moeda:.2f}'.replace('.', ',')
    else:
        return moeda


def diminuir(moeda, desconto=13, show=False):
    moeda -= (moeda * desconto) / 100
    if show:
        return f'R${moeda:.2f}'.replace('.', ',')
    else:
        return moeda


def resumo(moeda, aumento=80, redução=35):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Preço analisado:":<21}', end='')
    print(f'R${moeda:.2f}'.replace('.', ','))
    print(f'{"Dobro do preço:":<21}', end='')
    print(dobro(moeda, show=True))
    print(f'{"Metade do preço:":<21}', end='')
    print(metade(moeda, show=True))
    print(f'{aumento}{"% de aumento:":<19}', end='')
    print(aumentar(moeda, desconto=aumento, show=True))
    print(f'{redução}{"% de redução:":<19}', end='')
    print(diminuir(moeda, desconto=redução, show=True))
    print('-' * 30)


if __name__ == "__main__":
    print('Este arquivo acaba de ser executado como um script Python.')
    print("__name__: ", __name__)
else:
    print('Este arquivo acaba de ser importado como um módulo Python.')
    print("__name__: ", __name__)