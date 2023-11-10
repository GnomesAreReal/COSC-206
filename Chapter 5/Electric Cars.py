cars = (['blue'] * 4 +
        ['red'] * 8 +
        ['purple'] * 2 +
        ['white'] * 5 +
        ['topaz'] * 7 +
        ['silver'] * 2)

# 1
print('total cars: ' + str(len(cars)))
# 2
print('first: ' + cars[0], 'last: ' + cars[-1])
# 3
cars.insert(0, 'lime')
# 4
cars.pop(cars.index('silver'))
print(cars)
# 5
cars.remove('lime')
# 6
cars.remove('purple')
print(cars)
# 7
print(cars)