print("Lets play a simple game")
Loop = True
started = False
stopped = True
while Loop:
    question = input("Command>").lower()
    if question == "start":
         if started:
             print("The car is already on it's way")
         else:
             started = True
             stopped = False
             print("Please check your seatbelts")
             print("Here we go..................................................")
    elif question == "stop":
        if stopped:
            print('Wait....The car is already stopped!!!')
        else:
            stopped = True
            started = False
            print("Hold on tight.....")
            print("The car has stopped")
    elif question == "help":
        print("Type start to start the car.")
        print("Type stop to stop the car.")
        print("Type help to get the right commands")
        print("Type quit to quit the game")
    elif question == "quit":
        break
    else:
        print("Seems like the command is not registered in the server")
        print("Type Help to know the actual commands")
print("Have a good day ^_^")
print("~♥─▀██▀─▄███▄─▀██─██▀██▀▀▀█─♥~")
print("~♥──██─███─███─██─██─██▄█───♥~")
print("~♥──██─▀██▄██▀─▀█▄█▀─██▀█───♥~")
print("~♥─▄██▄▄█▀▀▀─────▀──▄██▄▄▄█-♥~.")
