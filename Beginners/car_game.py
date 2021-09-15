command = ""
car_started = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if car_started:
            print("Car is already started..")
        else:
            car_started = True
            print("Car is starting..")
    elif command == 'stop':
        if not car_started:
            print("Car is already stopped...")
        else:
            car_started = False
            print("car is stopped now.")
    elif command == 'quit':
        break
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to quit the car
        ''')
    else:
        print("Sorry, I don't understand. Try again")