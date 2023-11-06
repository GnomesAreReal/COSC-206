number = int(input())
i = ''

numberLate = 0
Line = 0
nextNum = number

while True:
    i = input()

    if nextNum > 999:
        nextNum = 1

    if i == 'TAKE':
        numberLate += 1
        nextNum += 1
        Line += 1
    elif i == 'SERVE':
        Line -= 1
    elif i == 'CLOSE':
        print(numberLate, Line, nextNum)
        numberLate = 0
        Line = 0
    if i == 'EOF':
        break
