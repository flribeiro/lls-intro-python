#!/usr/bin/env python
# coding: utf-8

# # Usando Python como calculadora

# In[ ]:


1 + 1


# In[ ]:


10 / 2


# In[ ]:


10 / 3


# In[ ]:


10 // 3


# In[ ]:


3 ** 2


# # Atribuição de valores a variáveis

# In[ ]:


variavel_exemplo = 1
print(variavel_exemplo)


# In[ ]:


variavel_exemplo = "um texto qualquer"
print(variavel_exemplo)


# In[ ]:


variavel_exemplo = "outro texto" # só um comentário
print(variavel_exemplo)


# In[ ]:


# Comentários servem pra você explicar o que seu código está fazendo.
# O sinal de igual (=) é chamado de sinal de atribuição, porque com ele podemos atribuir um valor a uma variável.
altura = 10
largura = 3
area = largura * altura
print(area)


# # Operações com strings (texto)

# In[ ]:


nome = "Fabrício"
sobrenome = "Ribeiro"

print(nome + sobrenome)


# In[ ]:


strlist = [nome, sobrenome]

print(" ".join(strlist))


# In[ ]:


multi_linhas = "primeira linha\nsegunda linha"
print(multi_linhas)


# In[ ]:


path="c:\diretorio\nomedoarquivo"
print(path)


# In[ ]:


path=r"c:\diretorio\nomedoarquivo"
print(path)


# In[ ]:


nome = "Ana"
idade = 22
cidade = "Franca"
linguagem = "Java"

print(f"""Olá, meu nome é {nome}, tenho {idade} anos e moro em {cidade}.
Estou aprendendo a programar em {linguagem}.""")


# In[ ]:


print("ba" + (2 * "na"))


# In[ ]:


empresa = "Magazine Luiza"


# In[ ]:


print(empresa[7])


# In[ ]:


print(empresa[-2])


# In[ ]:


print(empresa[:8])


# In[ ]:


print(empresa[9:])

  +---+---+---+---+---+---+---+---+---+---+---+---+---+---+
  | M | a | g | a | z | i | n | e |   | L | u | i | z | a |
  +---+---+---+---+---+---+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7   8   9   10  11  12  13  14
-14 -13 -12 -11 -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
# In[ ]:


print(empresa[15])


# In[ ]:


print(empresa[9:28])


# #### Desafio da Aula 01
# Faça o interpretador Python usar a string `empresa` para printar somente a palavra `MagaLu` no prompt.

# In[ ]:


print(?)


# # Operações com listas (arrays)

# In[ ]:


pares = [0, 2, 4, 6, 8, 10]
impares = [1, 3, 5, 7, 9]


# In[ ]:


pares[2]


# In[ ]:


impares[4]


# In[ ]:


pares + impares


# In[ ]:


impares[4] = 11


# In[ ]:


impares


# In[ ]:


impares.append(9)


# In[ ]:


impares


# In[ ]:


impares.remove(11)


# In[ ]:


impares


# In[ ]:


impares.pop()


# In[ ]:


impares


# In[ ]:


pares.index(2)


# In[ ]:


len(impares)


# In[ ]:


lista_qualquer = [0, 1, 2]
a, b, c = lista_qualquer


# In[ ]:


a


# In[ ]:


b


# In[ ]:


c


# # Primeiros passos na programação

# In[ ]:


# Sequência de Fibonacci (o próximo número é a soma do número atual + anterior)
while a < 35:
    print(a)
    a, b = b, a+b


# In[ ]:


a, b = 0, 1
while a < 35:
    print(a, end=', ')
    a, b = b, a+b


# In[ ]:


x = int(input("Digite um número de 0 a 100:"))


# In[ ]:


if x < 10:
    print("Número muito pequeno.")
elif x < 40:
    print("Número pequeno.")
elif x < 60:
    print("Número médio.")
elif x < 90:
    print("Número grande.")
else:
    print("Número gigante.")

