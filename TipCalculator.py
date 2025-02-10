print("Welcome to the tip calculator!")

bill = input("What was the total bill?$ ")
tip = input("How much tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")

float_bill = float(bill)
int_tip = int(tip)
int_people = int(people)

pay = (float_bill / int_people) * (1 + int_tip / 100)

pay = "{:.2f}".format(pay)

print(f"Each person should pay: {pay}$")

