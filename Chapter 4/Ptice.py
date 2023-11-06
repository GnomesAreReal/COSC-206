questions = int(input())
answers = input()

Adrian = 'ABC'
AdrianScore = 0
Bruno = 'BABC'
BrunoScore = 0
Goran = 'CCAABB'
GoranScore = 0

for i in range(questions):
    if answers[i] == Adrian[i % len(Adrian)]:
        AdrianScore += 1
    if answers[i] == Bruno[i % len(Bruno)]:
        BrunoScore += 1
    if answers[i] == Goran[i % len(Goran)]:
        GoranScore += 1

highscore = max(AdrianScore, BrunoScore, GoranScore)
print(highscore)
if AdrianScore == highscore:
    print('Adrian')
if BrunoScore == highscore:
    print('Bruno')
if GoranScore == highscore:
    print('Goran')