"""Meu primeiro porgrama em Python."""
import sys

def saudação(nome="aluno", args=''):
    print(f"Olá, {nome}!")
    if args:
        print(args)


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        saudação(args[1], args)
    else:
        saudação()