words = ''

while True:
    words = input()
    if words == 'quit!':
        break
    elif len(words) < 4 or words[-3] in 'aeiouy':
        print(words)
    elif words[-2:] == 'or':
        print(words[:-2] + 'our')
