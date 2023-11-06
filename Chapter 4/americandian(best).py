while True:
    input_text = input()
    if input_text == "quit!":
        break
    word = input_text.split()

    canada_word = []
    for word in word:
        if word.count('l') > 0 and word[word.rfind("l")-1] in 'aeiouy':
            word = (word[:word.rfind("l")] + "l" + word[word.rfind("l"):])
        if len(word) > 4 and word[-2:] == "or" and word[-3] not in "aeiouy":
            canada_word.append(word[:-2] + "our")
        elif word == "gray":
            canada_word.append(word.replace("a", "e"))
        elif word[-3:] == "yze":
            canada_word.append(word.replace("yze","ize"))
        elif word[-2:] == "er":
            canada_word.append(word[:-2]+ "re")
        elif word[-2:] == "se":
            canada_word.append(word[:-2] + "ce")
        elif word[-2:] == "og":
            canada_word.append(word[:-2] + "ogue")
        else:
            canada_word.append(word)

    canada_text = ' '.join(canada_word)

    print(canada_text)
