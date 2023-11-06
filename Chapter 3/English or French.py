# Get the number of lines
n = int(input())

S_count = 0
T_count = 0

for i in range(n):
    text = input()

    for t in range(text.count('t') + text.count('T')):
        T_count += 1
    for s in range(text.count('s') + text.count('S')):
        S_count += 1

if T_count > S_count:
    print("English")
else:
    print("French")