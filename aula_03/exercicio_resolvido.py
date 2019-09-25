import sys

def has_alphanumerical(s):
    for caractere in s:
        if caractere.isalnum():
            return True
    return False

def has_alphabetical(s):
    for caractere in s:
        if caractere.isalpha():
            return True
    return False

def has_digit(s):
    for caractere in s:
        if caractere.isdigit():
            return True
    return False

def has_lowercase(s):
    for caractere in s:
        if caractere.islower():
            return True
    return False

def has_uppercase(s):
    for caractere in s:
        if caractere.isupper():
            return True
    return False

if __name__ == '__main__':
    if len(sys.argv) > 1:
        s = sys.argv[1]
    else: 
        s = input('Digite um qualquer string: ')
    print(f'Possui caracter alfanumérico: {has_alphanumerical(s)}.')
    print(f'Possui caracter alfabético: {has_alphabetical(s)}.')
    print(f'Possui caracter dígito: {has_digit(s)}.')
    print(f'Possui caracter em caixa baixa: {has_lowercase(s)}.')
    print(f'Possui caracter em caixa alta: {has_uppercase(s)}.')