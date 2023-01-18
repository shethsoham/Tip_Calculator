print("Welcome to Tip calculator")
bill = float(input("What was the total bill  ?$"))
tip = int(input("How much percent tip will you like to give ?"))
people = int(input("Within how many people you want to split ?"))
tip_as_percentage = tip/100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person = total_bill/people
final_amount = round(bill_per_person,2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each Person should pay : ${final_amount}")