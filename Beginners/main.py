# weight = input("Enter your weight (lbs): ")
# weight_kg = int(weight) * 0.45
# print(weight_kg)
email = '''
Hello Dvs
This is the first multiline content
please try to print it

Thanks
'''
# print(email)

# -------- string operations
first = "Dvs"
last = "Bharadva"
msg = first + ' [' + last + '] is qualified for Canada PR'
message = f"{first} [{last}] is a Programmer"
# print(message)

# -------- string functions

course = "Pythong for Beginners"
# print(len(course))
# print(course.title())
# print(course.upper())
# print(course.lower())
# print(course.find('o'))
# print(course[1:15])
# print(course.find('for'))
# print(course.replace('Pythong', 'python'))
# print('for' in course)

# ------- arithmetic functions
#print(round(7.6))
#print(abs(-8))

#import math
#print(math.floor(4.9))
#print(math.ceil(5.1))

#---------------------- if else conditions

is_hot = False
if is_hot:
    print("It is a hot day")
    print("Drink plenty of water")
else:
    print("It's a cold day")
    print("wear a warm clothes")
print("enjoy your day")

#============= While loop - guess game
secret_number = 9
guess_limit = 5
guess_count = 0
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You won")
        break
else:
    print("Sorry! you failed")

def myname():
    name = input("enter name: ")


def display_name():
    print(myname() * 5)


# display_name()
