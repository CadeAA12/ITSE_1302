first_name = input("What is your first name? ")

last_name = input("What is your last name? ")

current_year = int(input("What is the current year? "))

birth_year = int(input("What is your birth year? "))

print()
age = current_year - birth_year

print("Hello, " + first_name, last_name,
"\nYou are", str(age), "this year." )

print()
age += 1

print(f"You will be {age} in {current_year + 1}")

print()

print("Completed by, Cade Armstrong")