words = ''

while words != 'quit!':
    words = input()

    if len(words) >= 4:
        for char in range(len(words)):
            if words[char:] == 'or' and words[char-1] not in 'aeiou':
                words = words[:char] + 'our'
    if words != 'quit!':
        print(words)