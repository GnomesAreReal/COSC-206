deck = ([11] * 4 + [2] * 4 + [3] * 4 + [4] * 4 + [5] * 4 + [6] * 4 + [7] * 4 + [8] * 4 + [9] * 4 + [10] * 4 + [10] * 4 + [10] * 4 + [10] * 4)

n = int(input())
drawn = []
for i in range(n):
    card = int(input())
    drawn.append(card)
    deck.remove(card)

x = 21 - sum(drawn)

numGreater = 0
numLower = 0
for cards in deck:
    if cards > x:
        numGreater += 1
    else:
        numLower += 1

if numGreater >= numLower:
    print('DOSTA')
else:
    print('VUCI')