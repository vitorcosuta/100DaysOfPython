#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the Tip Calculator")
total_bill = input("What was the total bill?  $")
percentage_tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
people_amount = input("How many people are going to split the bill? ")

#rounding the bill
total_bill = round(float(total_bill), 2)

percentage = f"1.{percentage_tip}"

tip_value = (total_bill / int(people_amount)) * float(percentage)
tip_value = "{:.2f}".format(tip_value)

print(f"Each person should pay ${tip_value}")
