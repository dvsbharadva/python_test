command = ""
car_state = ""
while True:
    car_state = command
    command = input("> ").lower()
    if command == 'start':
        print("Car is starting..")
    elif car_state == command == "start":
        print("hey, car is already started..")
    elif command == 'stop':
        print("Car is stopped now")
    elif car_state == command == "stop":
        print("Hey, car is already stopped..")
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