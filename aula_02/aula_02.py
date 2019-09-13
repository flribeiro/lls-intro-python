#!/usr/bin/env python
# coding: utf-8

# # Operações com listas (arrays)

# In[ ]:


pares = [0, 2, 4, 6, 8, 10]
impares = [1, 3, 5, 7, 9]
cores = ['vermelho', 'amarelo', 'azul']


# In[ ]:


pares[2]


# In[ ]:


impares[4]


# In[ ]:


pares + cores


# In[ ]:


impares[4] = 11

impares


# In[ ]:


impares.append(9)

impares


# In[ ]:


impares.remove(11)

impares


# In[ ]:


cores.insert(1, 'verde')

cores


# In[ ]:


cores.index('verde')


# In[ ]:


cores.count('verde')


# In[ ]:


cores.sort()
cores


# In[ ]:


cores.reverse()
cores


# In[ ]:


impares.pop()

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


# ##### Copiando uma lista

# In[ ]:


# Copiando uma lista
a = [1, 2, 3, 4, 5]
b = a


# In[ ]:


print('a: ', a)
print('b: ', b)


# In[ ]:


a[0] = 10
print(b)


# # Primeiros passos na programação

# ## Estruturas de controle de fluxo

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


x = int(input("Digite sua idade: "))
if x < 10:
    print("Baby!")
elif x < 20:
    print("Um(a) aborrecente.")
elif x < 30:
    print("Parabéns! Já é quase gente.")
elif x < 90:
    print("Olha, um adultinho!")
else:
    print("Salve, Matusalém!")


# In[ ]:


animais = ['cão', 'gato', 'papagaio', 'calopsita']

for animal in animais:
    print(animal, len(animal))


# ## List comprehensions

# In[ ]:


quadrados = []
for x in range(10):
    squares.append(x**2)

print(quadrados)


# In[ ]:


quadrados = list(map(lambda x: x**2, range(10)))

print(quadrados)


# In[ ]:


quadrados = [x**2 for x in range(10)]

print(quadrados)


# ## Range

# In[ ]:


for x in range(10):
    print(x)


# In[ ]:


for x in range(10, 20):
    print(x)


# In[ ]:


for x in range(10, 20, 2):
    print(x)


# In[ ]:


hino = ['Ouviram', 'do', 'Ipiranga', 'às', 'margens', 'plácidas']

for i in range(len(hino)):
    print(i, hino[i])


# Solução alternativa a essa:

# In[ ]:


for palavra in hino:
    print(palavra)


# In[ ]:


list(range(10))


# ## Cláusulas `break`, `continue` e `pass`

# In[ ]:


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'é o mesmo que', x, '*', n//x)
            break
    else:
        # o loop cai aqui quando não encontra um fator
        print(n, 'é um número primo')


# In[ ]:


for num in range(2, 10):
    if num % 2 == 0:
        print("Encontrei um número par: ", num)
        continue
    print("Encontrei um número: ", num)


# In[ ]:


while True:
    if (int(input()) == 1):
        pass
    else:
        break


# # Definindo funções em Python

# In[ ]:


def soma(a, b):
    """Retorna a soma de a + b."""
    return a + b


# In[ ]:


soma(10, 1)


# In[ ]:


def fibonacci(n):
    """Imprime a sequência de Fibonacci até o número n."""
    a, b = 0, 1
    while a < n: 
        print(a, end=' ')
        a, b = b, a+b
    print()


# In[ ]:


fibonacci(100000)


# ### Exercício de hoje:
# Alterar a função de fibonacci para, ao invés de imprimir na tela, retornar uma  lista com os resultados:

# In[ ]:


def fibonacci(n):
    """Retorna uma LISTA contendo a sequência de Fibonacci até o número n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# In[ ]:


# Teste
resultado_fibonacci = fibonacci(100)
print(resultado_fibonacci)


# ## Argumentos posicionais _(positional arguments)_

# In[ ]:


def nome_por_extenso(nome, sobrenome):
    print(f"{nome} {sobrenome}")


# In[ ]:


nome_por_extenso('Fabrício', 'Ribeiro')


# ## Argumentos padrão _(default arguments)_

# In[ ]:


def confirmação(mensagem, tentativas=4, alerta='Tente novamente!'):
    while True:
        resposta = input(mensagem)
        if resposta in ('s', 'si', 'sim', 'y', 'yep', 'yes'):
            return True
        if resposta in ('n', 'na', 'nop', 'não', 'no'):
            return False
        tentativas = tentativas - 1
        if retries < 0:
            raise ValueError('resposta inválida')
        print(reminder)


# In[ ]:


confirmação(
    "Deseja deletar todos os seus arquivos?",
    2,
    "Qual é cara?! É só sim ou não."
)


# ## Argumentos por palavras-chave _(keyword arguments ou kwargs)_

# In[ ]:


def labsschool(curso, nome='Fabrício', idade=36, empresa='Magalu'):
    print("Meu nome é", nome, end=' ')
    print("e estou aqui para aprender", curso, "com a galera.")
    print(f"Tenho {idade} anos e meu sonho é trabalhar na {empresa}.")


# In[ ]:


labsschool('Python')


# ## Lista de argumentos arbitrários

# In[ ]:


def lanchonete(lanche, *argumentos, **palavras_chave):
    print(f"-- Olá, boa noite. Gostaria de um {lanche} por favor.")
    print(f"-- Desculpe, mas hoje não estamos fazendo {lanche}.")
    for a in argumentos:
        print(a)
    print("-" * 40)
    for pc in palavras_chave:
        print(f"{pc}: {palavras_chave[pc]}")


# In[ ]:


lanchonete(
    "X-Burger",
    "Refrigerante",
    "Batata-frita",
    "hehehehehe",
    catchup=True,
    opcional="catupiry"
)


# ## Funções Lambda

# In[ ]:


f = lambda x: x * x


# In[ ]:


f(6)


# # Guia de Estilo - PEP 8
# 
# ### Principais pontos:

# * Indentação: 4 espaços (não usar Tab)
# * Quebre linhas (não ultrapassar 80 colunas)
# * Use linhas em branco para destacar classes, funções, e blocos de código dentro de funções
# * Sendo possível, coloque comentários em uma linha só pra isso
# * Use docstrings
# * Use espaços em torno de operadores e após as vírgulas, mas não dentro de parênteses (), colchetes [] ou chaves {}:
#     Ex.: `a = f(1, 2) + g(3, 4)`
# * Ao nomear classes em Python, use `CamelCase`
# * Ao nomear funções e variáveis, use `snake_case`
# * O primeiro argumento de um método de classe é sempre `self`
# * Encoding padrão: UTF-8
# * Não use caracteres não-ASCII para nomear qualquer coisa no seu código, por motivos óbvios
