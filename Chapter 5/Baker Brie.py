for _ in range(10):
    Franchises, Days = map(int, input().split())

    grid = []
    dozens = 0

    for i in range(Days):
        grid.append(list(map(int, input().split())))

    for row in grid:
        # Sum of all franchises for the day
        if sum(row) % 13 == 0:
            dozens += sum(row) // 13

    for col_index in range(Franchises):
        column = []
        for row_index in range(Days):
            column.append(grid[row_index][col_index])

        if sum(column) % 13 == 0:
            dozens += sum(column) // 13

    print(dozens)
