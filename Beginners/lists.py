#names = ['abc', 'bcd', 'cde', 'def', 'efg']
#print(names)
#print(names[3])
#print(names[3:5])
#names[2] = "john"
#print(names)

#find the maximum number
#numbers = [10, 15, 22, 1, 14, 17, 25, 24, 28]
#temp_store = numbers[0]
#for x in numbers:
#    if x > temp_store:
#        temp_store = x
#print(temp_store)

#unique number:
#numbers = [7, 4, 3, 7, 5, 3, 3, 2]
#unique = []
#for number in numbers:
#    if number not in unique:
#        unique.append(number)
#print(unique)

#digit in word
phone = input("Enter number: ")
words = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero"
}
output = ""
for number in phone:
    output += words.get(number, number) + " "

print(output)