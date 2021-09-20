#for characters in "Python":
#    print(characters)

#for items in ["abc", "bcd", "cde", "def"]:
    #print("item: "+ items)

#for items in range(5):
    #print(items)

#for items in range(3,10):
#    print(items)

#for items in range(3,10, 2):
#    print(items)

#shopping cart items total
#cart = [10,20, 25, 35, 50]
#total = 0
#for item in cart:
#    total = total + item
#print(f"Total cost is: {total}")

#Nested for loop
#for row in range(5):
#    for column in range(5):
#        print(f" ({row}, {column})")

#challenge
pattern = [5,2,5,2,2]
#for x in pattern:
#    print("X" *x)

for x in pattern:
    output = ""
    for y in range(x):
        output += "X"
    print(output)