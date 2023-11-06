P = int(input())
B = int(input())
D = int(input())

badges_painted = P // B
paint_leftover = int(P % B)
result = (badges_painted * D) + paint_leftover
print(result)
