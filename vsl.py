# Topic: If-Else Condition (Roller Coaster Eligibility)
age = int(input("Enter your age: "))
height = int(input("Enter your height in cm: "))

if age >= 12 and height >= 140:
    print("You can ride the roller coaster.")
else:
    print("You cannot ride the roller coaster.")

# Topic: If-Elif-Else (Traffic Light System)
light = input("Enter traffic light color (red/yellow/green): ").lower()

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Get Ready")
elif light == "green":
    print("Go")
else:
    print("Invalid color")

# Topic: Match Case Statement (Season Program)
num = int(input("Enter a number (1-4): "))

if num == 1:
    print("Spring")
elif num == 2:
    print("Summer")
elif num == 3:
    print("Autumn")
elif num == 4:
    print("Winter")
else:
    print("Unknown")

# Topic: Nested If (Login System)
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin":
    if password == "pass123":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")

# Topic: Multiple Conditions (Bank Loan Approval)
age = int(input("Enter age: "))
income = int(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))

if age < 21 or age > 60:
    print("Loan rejected: Age condition failed")
elif income < 30000:
    print("Loan rejected: Income condition failed")
elif credit_score < 700:
    print("Loan rejected: Credit score condition failed")
else:
    print("Loan Approved")

# Topic: Nested If-Else (Movie Ticket System)
age = int(input("Enter age: "))
membership = input("Do you have membership card (yes/no): ").lower()

if age < 12:
    price = 0
elif age <= 60:
    if membership == "yes":
        price = 150
    else:
        price = 200
else:
    price = 100

print("Ticket price:", price)

# Topic: Simple If Condition (Employee Bonus)
salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if years > 5:
    bonus = salary * 0.05
    print("Bonus amount:", bonus)
else:
    print("No bonus")

# Topic: Mathematical Calculation (Area of Circle)
radius = float(input("Enter radius: "))

area = 3.14 * radius * radius

print("Area of circle:", area)

# Topic: If-Else with Multiple Conditions (Wage Calculation)
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
days = int(input("Enter number of days: "))

if age >= 18 and age < 30:
    if gender == "M":
        wage = 700
    else:
        wage = 750

elif age >= 30 and age <= 40:
    if gender == "M":
        wage = 800
    else:
        wage = 850

total = wage * days
print("Total wages:", total)

# Topic: If-Elif-Else with Modulus (Fizz Buzz)
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Fizz Buzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)