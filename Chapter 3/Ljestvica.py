notes = input()

Amin = 0
Cmaj = 0
lastNote = '|'

for i in range(len(notes)):
    if i == 0 or notes[i-1] == '|':
        if notes[i] == 'A' or notes[i] == 'D' or notes[i] == 'E':
            Amin += 1
        elif notes[i] == 'C' or notes[i] == 'F' or notes[i] == 'G':
            Cmaj += 1

if Cmaj > Amin:
    print("C-dur")
elif Amin > Cmaj:
    print("A-mol")
elif Cmaj == Amin:
    if notes[-1] == 'A':
        print("A-mol")
    elif notes[-1] == 'C':
        print("C-dur")