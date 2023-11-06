wand_owner = input()
duel_num = int(input())

total_owners = 1
owned = wand_owner

for i in range(duel_num):
    duel = input()

    if duel[2] == wand_owner:
        if duel[0] not in owned:
            total_owners += 1
            owned += duel[0]

        wand_owner = duel[0]

print(wand_owner)
print(total_owners)
