amounts = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
opened_cases = int(input())
for i in range(opened_cases):
    amounts[int(input())-1] = 0
offer = int(input())

for i in amounts:
    if i == 0:
        amounts.remove(i)

unopened_cases = sum(amounts) / len(amounts)

if offer > unopened_cases:
    print('deal')
else:
    print('no deal')

