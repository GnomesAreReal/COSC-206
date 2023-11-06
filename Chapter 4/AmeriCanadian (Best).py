while True:
    word = input()
    if word == 'quit!':
        break
    elif len(word) > 4 and word[-2:] == 'or' and word[-3] not in 'aeiouy':
        print(word[:-2] + 'our')
    else:
        print(word)