Franchises, Days = map(int, input().split())

grid = []
bonuses = 0

for i in range(Days):
    grid.append(list(map(int, input().split())))
print(grid)

for row in grid:
    # Sum of all franchises for the day
    if sum(row) % 13 == 0:
        bonuses += sum(row) // 13
print(bonuses)