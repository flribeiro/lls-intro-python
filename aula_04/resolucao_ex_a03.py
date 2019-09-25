"""Solução por Matheus da Silva Rodrigues."""

import sys

def has_alphanumerical(s):
    retorno = False
    for i in s:
        if i.isalnum():
            retorno = True        
    return retorno 

def has_alphabetical(s):
    retorno = False
    for i in s:
        if i.isalpha():
            retorno = True        
    return retorno 

def has_digit(s):
    retorno = False
    for i in s:
        if i.isdigit():
            retorno = True        
    return retorno  

def has_lowercase(s):
    retorno = False
    for i in s:
        if i.islower():
            retorno = True        
    return retorno 

def has_uppercase(s):
    retorno = False
    for i in s:
        if i.isupper():
            retorno = True        
    return retorno

def FormataTexto(s):
    alfanumerico = has_alphanumerical(s)
    alfabetico = has_alphabetical(s)
    digito = has_digit(s)
    lower = has_lowercase(s)
    upper = has_uppercase(s)

    print(f'\033[1;34;40m{"-" *40}\033[m' )
    print(f'\033[1;30;40m{s:^40}\033[m')
    print(f'\033[1;34;40m{"-" *40}\033[m' )

    if(alfanumerico):
        print(f'\033[1;32;40m{"É alfanúmerico:":<36}\033[m', end='')
        print(f'\033[1;32;40m{alfanumerico}\033[m')
    else:
        print(f'\033[1;31;40m{"É alfanúmerico:":<35}\033[m', end='')
        print(f'\033[1;31;40m{alfanumerico}\033[m')

    if(alfabetico):
        print(f'\033[1;32;40m{"É alfabético:":<36}\033[m', end='')
        print(f'\033[1;32;40m{alfabetico}\033[m')
    else:
        print(f'\033[1;31;40m{"É alfabético:":<35}\033[m', end='')
        print(f'\033[1;31;40m{alfabetico}\033[m')

    if(digito):
        print(f'\033[1;32;40m{"É digito:":<36}\033[m', end='')
        print(f'\033[1;32;40m{digito}\033[m')
    else:
        print(f'\033[1;31;40m{"É digito:":<35}\033[m', end='')
        print(f'\033[1;31;40m{digito}\033[m')

    if(lower):
        print(f'\033[1;32;40m{"Contem letras em minusculo:":<36}\033[m', end='')
        print(f'\033[1;32;40m{lower}\033[m')
    else:
        print(f'\033[1;31;40m{"Contem letras em minusculo:":<35}\033[m', end='')
        print(f'\033[1;31;40m{lower}\033[m')

    if(upper):
        print(f'\033[1;32;40m{"Contem letras em maiusculo:":<36}\033[m', end='')
        print(f'\033[1;32;40m{upper}\033[m')
    else:
        print(f'\033[1;31;40m{"Contem letras em maiusculo:":<35}\033[m', end='')
        print(f'\033[1;31;40m{upper}\033[m')
        
    print(f'\033[1;34;40m{"-" *40}\033[m' )

if __name__ == '__main__':
    """ Passe como argumento de linha de comando, uma 
    string qualquer. Depois impirmi na tela o seguinte:
    TRUE - se algum dos catacteres da stribg for alfanúmerico
    TRUE - se algum dos caracteres da string for alfabético 
    TRUE - se algum dos caracteres da string for digito
    TRUE - se algum dos caracteres da string for minusculo
    TRUE - se algum dos caracteres da string for maiusculo
    Para todos os casos, imprimir False do contrário. """

    lista = sys.argv

    if(len(lista) < 2):
        print('Por favor, digite algum parametro!.')
    else:
        FormataTexto(sys.argv[1])