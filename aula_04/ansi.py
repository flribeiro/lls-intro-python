cores = (
    '\033[m',  # 0 – Sem cor
    '\033[0;30;41m',  # 1 – Vermelho
    '\033[0;30;42m',  # 2 – Verde
    '\033[0;30;43m',  # 3 – Amarelo
    '\033[0;30;44m',  # 4 – Azul
    '\033[0;30;45m',  # 5 – Roxo
    '\033[7;30m')  # 6 – Branco


def título(msg, cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


título('LabsSchool Python', 2)
