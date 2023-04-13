import random

class TrainReservation:
    def __init__(self, name, age, boarding, arrival):
        self.name = name
        self.age = age
        self.boarding = boarding
        self.arrival = arrival

    def TrainChecking(self):
        RajAvail = random.randint(1, 150)
        GaribRathAvail = random.randint(1, 150)
        if(RajAvail<100 and GaribRathAvail<100): 
            x = str(input("Rajdhani And GribRath is available press (r) for Rajdhani or press (G) for GaribRath: "))
            if (x == "r"):
                print("\n-------------------")
                print("\nPassenger Name: " + self.name)
                print("Passenger Age: " + str(self.age))
                print("Boarding: " + self.boarding)
                print("Arrival: " + self.arrival)
                print("Train: Rajdhani Express")
                print("Confirmed")  
                exit()

            if ( x == "g"):
                print("\n-------------------")
                print("\nPassenger Name: " + self.name)
                print("Passenger Age: " + str(self.age))
                print("Boarding: " + self.boarding)
                print("Arrival: " + self.arrival)
                print("Train: GaribRath Express")
                print("Confirmed")
                exit()





        if RajAvail >= 100:
            pass
        else:
            c1 = str(input("Rajdhani is available. Press (r) to confirm: "))
            if c1 == "r":
                print("\n-------------------")
                print("\nPassenger Name: " + self.name)
                print("Passenger Age: " + str(self.age))
                print("Boarding: " + self.boarding)
                print("Arrival: " + self.arrival)
                print("Train: Rajdhani Express")
                print("Confirmed")
                exit()
            else:
                print("Invalid Option")
               

        if GaribRathAvail >= 100:
           pass
        else:
            c2 = str(input("GaribRath is available. Press (g) to confirm: "))
            if c2 == "g":
                print("\n-------------------")
                print("\nPassenger Name: " + self.name)
                print("Passenger Age: " + str(self.age))
                print("Boarding: " + self.boarding)
                print("Arrival: " + self.arrival)
                print("Train: GaribRath Express")
                print("Confirmed")
                exit()
            else:
                print("Invalid Option")
                
        if(RajAvail<100 and GaribRathAvail<100): 
            x = str(input("Rajdhani And GribRath is available press (r) for Rajdhani or press (G) for GaribRath"))
            if (x == "r"):
                print("\n-------------------")
                print("\nPassenger Name: " + self.name)
                print("Passenger Age: " + str(self.age))
                print("Boarding: " + self.boarding)
                print("Arrival: " + self.arrival)
                print("Train: Rajdhani Express")
                print("Confirmed")  
                exit()

            if ( x == "g"):
                print("\n-------------------")
                print("\nPassenger Name: " + self.name)
                print("Passenger Age: " + str(self.age))
                print("Boarding: " + self.boarding)
                print("Arrival: " + self.arrival)
                print("Train: GaribRath Express")
                print("Confirmed")
                exit()


pname = str(input("Enter The Passenger Name: "))  
page = int(input(f"Hello {pname} How Old Are You: "))
pboarding = str(input("Where is your boarding from? "))
parrival = str(input("Where is your arrival? ")) 

Passenger = TrainReservation(pname, page, pboarding, parrival)
Passenger.TrainChecking()
