N = input()

count = 0
state = 0

for char in range(len(N)):
    if N[char] == 'H' and state == 0:
        state += 1
    elif N[char] == 'O' and state == 1:
        state += 1
    elif N[char] == 'N' and state == 2:
        state += 1
    elif N[char] == 'I' and state == 3:
        count += 1
        state = 0

print(count)