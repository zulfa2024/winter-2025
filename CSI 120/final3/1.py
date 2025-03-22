
# Prompt the user to input 5 tuples (name, age)
print("Please enter 5 tuples, each containing a name and an age.")
people = []

for i in range(5):
    name = input(f"Enter name for person {i + 1}: ")
    age = int(input(f"Enter age for person {i + 1}: "))
    people.append((name, age))

# Check if anyone is above 18 years old
print("\nPeople above 18 years old:")
above_18_found = False
for person in people:
    if person[1] > 18:
        print(person[0])
        above_18_found = True

if not above_18_found:
    print("No one is above 18 years old.")