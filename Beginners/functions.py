import random

def user_details(first_name, last_name):
    print(f'Hello {first_name} {last_name}!')
    print("How are you!!")


user_details(first_name="Divyesh", last_name="Bharadva")

for x in range(5):
    print(random.randint(1, 20))

participant = ["Divyesh", "Maanav", "Hiren", "Shakti"]
leader = random.choice(participant)
print(f"Today's leader is: {leader}")


class Dice:
    def role(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return  first, second


turn_dice = Dice()
print(turn_dice.role())