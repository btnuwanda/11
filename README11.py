

    def __init__(self):
        self.lines = {}
        self.trains = {}

    def add_train(self):
        while True:
            name = input("Enter name or back")
            if name.lower() == "back":
                print("Returning to the panel")
                return

            if name in self.trains:
                print("The name already exists")
                continue

            line = input("Enter line name or back")
            if line.lower() == "back":
                print("Returning to the panel")
                return
            if line not in self.lines:
                print("The Line doesn't exist")
                continue


            while True:
                avr_speed = input("Enter average speed or back ")
                if avr_speed.lower() == "back":
                    print("Returning to the panel")
                    return
                if speed_input.isdigit():
                    speed = float(speed_input)
                    break
                else:
                    print("Please enter a valid number")

            
            while True:
                stop_time = input("Enter stop time or back")
                if stop_time.lower() == "back":
                    print("Returning to the panel")
                    return
                if stop_time.isdigit():
                    stop = float(stop_input)
                    break
                else:
                    print("Please enter a valid number")