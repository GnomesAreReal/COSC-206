monthly_mb = int(input())
months = int(input())

excess = 0

for i in range(months):
    used = int(input())
    excess = monthly_mb + excess - used

print(excess + monthly_mb)