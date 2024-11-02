command=""
started= False
stopped=False
while True:
    command= input(">").lower()
    if command== "help":
        print('''start= start the car
stop= stop car
quit= exit the car''')
    elif command== "start":
        if started:
            print("already started")
        else:
            print("started")
            started= True
    elif command== "stop":
        if stopped or not started:
            print("already stopped")
        else:
            print("stopped")
            stopped= True
    elif command=="quit":
        pass
    else:
        print("cant recognize")
