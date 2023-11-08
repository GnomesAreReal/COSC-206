amounts = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
n = int(input())
selected_cases = []
for i in range(n):
    selected_cases.append(amounts[int(input()) - 1])
offer = int(input())

for i in range(len(selected_cases)):
    amounts.remove(selected_cases[i])

average = sum(amounts) / len(amounts)

if offer > average:
    print('deal')
else:
    print('no deal')