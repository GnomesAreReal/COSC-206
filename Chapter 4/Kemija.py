code = input()
output = ''
i = 0
while i < len(code):
    output += code[i]
    if code[i] in 'aeiou':
        i += 3
    else:
        i += 1
print(output)