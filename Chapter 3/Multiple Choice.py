n = int(input())

answers = []
solutions = []

# Get the inputs
for a in range(n):
    answers += input()
for s in range(n):
    solutions += input()

correct = 0
for i in range(n):
    if answers[i] == solutions[i]:
        correct += 1
print(correct)