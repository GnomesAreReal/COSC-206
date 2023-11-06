quarters = int(input())
machine1 = int(input())
machine2 = int(input())
machine3 = int(input())

played = 0

while quarters >= 1:
    machine = played % 3
    quarters -= 1
    played += 1

    if machine == 0:
        machine1 += 1
        if machine1 % 35 == 0:
            quarters += 30
    elif machine == 1:
        machine2 += 1
        if machine2 % 100 == 0:
            quarters += 60
    elif machine == 2:
        machine3 += 1
        if machine3 % 10 == 0:
            quarters += 9

print(f'Martha plays {played} times before going broke.')
