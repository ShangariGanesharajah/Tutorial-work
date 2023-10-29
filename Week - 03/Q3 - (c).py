meal_cost = float(input("Enter the cost of the meal: "))
satisfaction_level = int(input("Rate your satisfaction (1 = Totally satisfied, 2 = Satisfied, 3 = Dissatisfied): "))
if satisfaction_level == 1:
    tip_percentage = 20
elif satisfaction_level == 2:
    tip_percentage = 15
elif satisfaction_level == 3:
    tip_percentage = 10
else:
    print("Invalid satisfaction level entered. Please enter 1, 2, or 3.")
    exit() 
tip_amount = (tip_percentage / 100) * meal_cost
print(f"Satisfaction level: {satisfaction_level}")
print(f"Tip amount: {tip_amount:.2f}")