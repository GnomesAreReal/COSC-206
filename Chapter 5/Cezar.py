deck = ([11] + [2] + [3] + [4] + [5] + [6] + [7] + [8] + [9] + [10] + [10] + [10] + [10])
deck = deck * 4

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