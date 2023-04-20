jogadores = ['player 1', 'player 2', 'Player 3', 'player 4', 'player 5']
print(jogadores[0:3])
print(jogadores[1:2])
print(jogadores[:2])
print(jogadores[2:])
print("\n ---------------------------- \n")
jogadoresCopy = jogadores[:]
print('Cópia', jogadoresCopy)
print("\n ---------------------------- \n")
print(jogadores[-3:])
print(jogadores[3:])
print(jogadores[:3])
print(jogadores[:-3])
print("\n ---------------------------- \n")

print("\n ---------------------------- \n")
numbers = []
rangeNumbers = range(0, 10)
for number in rangeNumbers:
    numbers.append(number)
print(numbers[0:10:2])

print("\n ---------------------------- \n")

print('Lista de players:\n')
for player in jogadores[:3]:
    print(player.title())

print("\n ---------------------------- \n")

print('Lista de players:\n')
placar = [['Player 1', 1020], ['Player 2', 800], ['Player 3', 759], ['Player 4', 1250]]
for player in placar:
    print('Jogador:', player[0], ' / Pontos: ', player[1])
