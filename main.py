#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bills = float(input("What was the total bill? $"))
percent = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
split = int(input("How many people to split the bill? "))
# bill_percent = bills * (percent/100)
# total_pay = bill_percent + bills
#another way
total_pay = bills * (1 + (percent/100))
split_bill = round(total_pay/split,2)
split_bill_format = "{:.2f}".format(split_bill)

print(f"Each person should pay: ${split_bill_format}")
