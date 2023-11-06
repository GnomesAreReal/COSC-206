Population = int(input())
Infectious = int(input())
Infectiousness = int(input())
days = 0
total_infected = Infectious

while total_infected <= Population:
    Infectious *= Infectiousness
    total_infected += Infectious
    days += 1

print(days)