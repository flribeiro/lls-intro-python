jogador = dict()  # ou {}
partidas = list()  # ou ()

jogador['nome'] = str(input('Nome do Jogador: '))
total_partidas = int(input(f'Quantas partidas o(a) {jogador["nome"]} jogou? '))
for contador in range(0, total_partidas):
    partidas.append(int(input(f'Quantos gols na partida {contador}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)

# Visualização do dicionário completo
print('-=' * 30)
print(jogador)
print('-=' * 30)

for chave, valor in jogador.items():
    print(f'O campo {chave} tem o valor {valor}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} patidas.')
for chave, valor in enumerate(jogador['gols']):
    print(f'=> Na partida {chave}, fez {valor} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
