import random
# Define the size of the deck

NUM_CARDS = 52
deck = (['one'] * 4 +
        ['two'] * 4 +
        ['three'] * 4 +
        ['four'] * 4 +
        ['five'] * 4 +
        ['six'] * 4 +
        ['seven'] * 4 +
        ['eight'] * 4 +
        ['nine'] * 4 +
        ['ten'] * 4 +
        ['jack'] * 4 +
        ['queen'] * 4 +
        ['king'] * 4 +
        ['ace'] * 4)

random.shuffle(deck)

def no_high(lst):
    """
    lst is a list of strings representing cards.
    Return True if there are no high cards in lst, False otherwise
    """
    if 'jack' in lst:
        return False
    if 'queen' in lst:
        return False
    if 'king' in lst:
        return False
    if 'ace' in lst:
        return False
    return True




# Fill the deck with cards based on an input
# for i in range(NUM_CARDS):
#     deck.append(input())

# Declare total scores and current player
score_a, score_b = 0, 0
player = 'A'

for i in range(NUM_CARDS):
    card = deck[i]
    points = 0
    remaining = NUM_CARDS - i - 1
    if card == 'jack' and remaining >= 1 and no_high(deck[i+1:i+2]):
        points = 1
    elif card == 'queen' and remaining >= 2 and no_high(deck[i+1:i+3]):
        points = 2
    elif card == 'king' and remaining >= 3 and no_high(deck[i+1:i+4]):
        points = 3
    elif card == 'ace' and remaining >= 4 and no_high(deck[i+1:i+5]):
        points = 4

    if points > 0:
        print(f'Player {player} scores {points} point(s).')

    # Add to the total score and switch the active player
    if player == 'A':
        score_a += points
        player = 'B'
    else:
        score_b += points
        player = 'A'

print(f'Player A: {score_a} point(s).')
print(f'Player B: {score_b} point(s).')