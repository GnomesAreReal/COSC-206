for i in range(10):
    T, N = input().split()
    T, N = int(T), int(N)

    days = 0

    for i in range(N):
        if input() == 'B':
            days += T

        if days > 0:
            days -= 1

    print(days)