password = input()

lowercase, uppercase, digits = 0, 0, 0

for char in password:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isnumeric():
        digits += 1

if lowercase >= 3 and uppercase >= 2 and digits >= 1 and 8 <= len(password) <= 12:
    print("Valid")
else:
    print("Invalid")