button = 0
# songs = 'ABCDE'
songs = ("Creeper", "Don't Mine at Night", "Fallen kingdom", "Butter", "TNT")

while button != 4:
    button = int(input())
    numPresses = int(input())

    for i in range(numPresses):
        if button == 1:
            songs = songs[1:] + songs[0]
        elif button == 2:
            songs = songs[-1] + songs[:-1]
        elif button == 3:
            songs = songs[1] + songs[0] + songs[2:]

output = ''
for char in songs:
    output += char + ' '
print(output)