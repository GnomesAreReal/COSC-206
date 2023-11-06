combination = input()

location = 1

for char in combination:
    if char == 'A' and location == 1:
        location = 2
    elif char == 'A' and location == 2:
        location = 1
    elif char == 'B' and location == 2:
        location = 3
    elif char == 'B' and location == 3:
        location = 2
    elif char == 'C' and location == 1:
        location = 3
    elif char == 'C' and location == 3:
        location = 1

print(location)