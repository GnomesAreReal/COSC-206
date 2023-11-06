burger_choice = int(input())
side_choice = int(input())
drink_choice = int(input())
dessert_choice = int(input())

calories = 0

# Burger choices
if burger_choice == 1:
    calories += 461
elif burger_choice == 2:
    calories += 431
elif burger_choice == 3:
    calories += 420

# Side choices
if side_choice == 1:
    calories += 100
elif side_choice == 2:
    calories += 57
elif side_choice == 3:
    calories += 70

# Drink choices
if drink_choice == 1:
    calories += 130
elif drink_choice == 2:
    calories += 160
elif drink_choice == 3:
    calories += 118

# Dessert choices
if dessert_choice == 1:
    calories += 167
elif dessert_choice == 2:
    calories += 266
elif dessert_choice == 3:
    calories += 75

print('Your total Calorie count is ' + str(calories) + '.')