w1 = int(input())
w2 = int(input())
w3 = int(input())

if w2 <= w1 <= w3:
    print(str(w1))
elif w3 <= w1 <= w2:
    print(str(w1))
elif w1 <= w2 <= w3:
    print(str(w2))
elif w3 <= w2 <= w1:
    print(str(w2))
elif w1 <= w3 <= w2:
    print(str(w3))
elif w2 <= w3 <= w1:
    print(str(w3))