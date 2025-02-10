import os
# First set of inputs and calculations
years_of_service = int(input("Enter years of service: "))
current_salary = float(input("Enter current salary: "))

if years_of_service < 3:
    bonus_percentage = 0
elif 3 <= years_of_service <= 5:
    bonus_percentage = 10
elif 6 <= years_of_service <= 10:
    bonus_percentage = 20
else:
    bonus_percentage = 30

bonus_amount = current_salary * (bonus_percentage / 100)
total_salary_after_bonus = current_salary + bonus_amount

print(f"Bonus: {bonus_percentage}%")
print(f"Bonus Amount: ${bonus_amount}")
print(f"Total Salary after Bonus: ${total_salary_after_bonus}")

# Asking the user if they want to continue
continue_choice = input("Do you want to enter another set of values? (y/n): ").lower()
if continue_choice == 'y':
    # Second set of inputs and calculations
    years_of_service = int(input("Enter years of service: "))
    current_salary = float(input("Enter current salary: "))

    if years_of_service < 3:
        bonus_percentage = 0
    elif 3 <= years_of_service <= 5:
        bonus_percentage = 10
    elif 6 <= years_of_service <= 10:
        bonus_percentage = 20
    else:
        bonus_percentage = 30

    bonus_amount = current_salary * (bonus_percentage / 100)
    total_salary_after_bonus = current_salary + bonus_amount

    print(f"Bonus: {bonus_percentage}%")
    print(f"Bonus Amount: ${bonus_amount}")
    print(f"Total Salary after Bonus: ${total_salary_after_bonus}")
