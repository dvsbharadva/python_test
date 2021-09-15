total_price = 1000000
good_credit = True
eligible = False
has_criminal_record = True

if good_credit:
    print(f"Total down payment is: {total_price * 0.1}")
elif not good_credit or has_criminal_record:
    print("Person is not eligible for loan")
else:
    print(f"total down payment should be: {total_price * 0.2}")

print("how a nice day!")

#==== name length validation ====

#name = input("Enter your name: ")
name = "Dvs"
if len(name) <= 3:
    print("Please enter more than 3 character")
elif len(name) >= 10:
    print("please enter less than 10 character")
else:
    print("Name looks good")

#======= weight converter program =======
weight = int(input("Enter your weight: "))
convert_into = input("Convert into LBS (L) or KG (K): ")

if convert_into.upper() == 'K':
    print(f"your weight in kg: {weight * 0.45}")
elif convert_into.upper() == 'L':
    print(f"Your weight in LBS is: {weight / 0.45}")
else:
    print("You entered the wrong choice: "+ convert_into)