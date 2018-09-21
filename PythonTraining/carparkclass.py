import classcar

class CarPark(object):

    # define static members of the class here
    numberofParkingSpaces=10

    def __init__(self):
        # initialize the members of the carPark garage here!
        self.garage={}
        for i in range(1,CarPark.numberofParkingSpaces):
            self.garage.update({i:'FREE'})

        print(self.garage.items())
        self.numberofOpenSpaces=CarPark.numberofParkingSpaces
        self.parkingAmountCollected=0

    # define methods to be supported by CarPark Class
    def numberofOpenLots(self):
        return self.numberofOpenSpaces

    def printParkingSummary(self):
        print(self.garage.items())

    def parkcar(self, acar):
        # functionality to park a car
        if (self.numberofOpenSpaces == 0):
            print("garage is full, sorry you can't park")
        else:
            # find empty lot and park it there!
            for i in range(1, CarPark.numberofParkingSpaces):
                if self.garage[i] == 'FREE':
                    --self.numberofOpenSpaces
                    self.garage[i] = acar.getlicenseno()
                    break

    def retrievecar(self, acar):
        # functionality to retrieve car from parking
        for key,val in self.garage.items():
            if (acar.getlicenseno() == val):
                # car found, free up spot
                self.garage[key] = "FREE"
                ++self.numberofOpenSpaces
                break

    def _retrieveParkingTicket(self):
        # captures details around card parked timing etc.,
        pass

    def _payforParkingTicket(self):
        # tender payment based on amount of time car parked
        pass

# Test CarPark
parkgarage=CarPark()
print("number of open lots - ", parkgarage.numberofOpenLots())

mycar=classcar.car("NY1000", 100, 40)
myfamilycar=classcar.familycar("FM1000", 100,  60,2)
myluxarycar=classcar.luxarycar("LX1000", 100, 70)
mysportscar=classcar.sportscar("SP1000", 120, 90)
myluxarysportscar=classcar.luxarysportscar("LSP1000", 120,  90)

parkgarage.parkcar(mycar)
print("number of open lots - ", parkgarage.numberofOpenLots())
parkgarage.retrievecar(mycar)
print("number of open lots - ", parkgarage.numberofOpenLots())
parkgarage.printParkingSummary()

parkgarage.parkcar(myfamilycar)
parkgarage.parkcar(myluxarycar)
parkgarage.parkcar(mysportscar)
parkgarage.parkcar(myluxarysportscar)
print("number of open lots - ", parkgarage.numberofOpenLots())
parkgarage.printParkingSummary()



