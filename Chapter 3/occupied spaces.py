n = int(input())
yesterday = input()
today = input()

occupied = 0

for i in range(n):
    if yesterday[i] == today[i] == 'C':
        occupied += 1

print(occupied)