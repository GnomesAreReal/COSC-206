costs = [12, 10, 7, 5]
for data in range(10):
    total_cost = int(input())
    percents = input().split()
    students = int(input())

    for years in range(len(percents)):
        percents[years] = float(percents[years])

    students_per_year = []
    for i in range(len(percents)):
        students_per_year.append(students * percents[i])
    print(students_per_year)

    raised_funds = 0
    for i in range(4):
        raised_funds += students * percents[i] * costs[i]

    if raised_funds / 2 < total_cost:
        print('YES')
    else:
        print('NO')