class car(object):

    # constructor
    def __init__(self, regno, topspeed, initialspeed):
        self.speed=initialspeed
        self.registrationno=regno
        self.topspeed=topspeed

    # accessors
    def getspeed(self):
        return self.speed

    def getlicenseno(self):
        return self.registrationno

    # action method
    def accelerate(self):
        if(self.speed > self.topspeed):
            print("You are crossing maximum speed, which is not allowed, max speed is ", self.topspeed, " you are trying ", speed)
        else:
            self.speed+=5

    def gettopspeed(self):
        return self.topspeed

# Create inheritance classes
# faily car
class familycar(car):

    # constructor
    def __init__(self, regno, topspeed, initialspeed, numberofseatbelts):
        super().__init__(regno, topspeed, initialspeed)
        if (numberofseatbelts <= 0 ):
            print("Get some seat belts, it is not safe to drive without seat belts for family")
        self.numberofseatbelts=numberofseatbelts

    def accelerate(self):
        if(self.numberofseatbelts <=0):
            print("no Seat belts, so cant accelerate")
        else:
            car.accelerate(self)

# luxary car
class luxarycar(car):

    # constructor
    def __init__(self, regno, topspeed, initialspeed):
        super().__init__(regno, topspeed, initialspeed)

# sports car
class sportscar(car):

    # constructor
    def __init__(self, regno, topspeed, initialspeed):
        super().__init__(regno, topspeed, initialspeed)

# luxary sports car
class luxarysportscar(luxarycar, sportscar):

    # constructor
    def __init__(self, regno, topspeed, initialspeed):
        super().__init__(regno, topspeed, initialspeed)

if __name__ == "__main__":

    # Test code to call the class
    mycar=car("NY1000", 100, 40)
    print("license plate number - ", mycar.getlicenseno())
    print("current speed - ", mycar.getspeed())
    mycar.accelerate()
    print("current speed - ", mycar.getspeed())
    mycar.accelerate()
    print("current speed - ", mycar.getspeed())

    # Test out inheritence
    myfamilycar=car("FM1000", 100, 60)
    print("familycar - license plate number - ", myfamilycar.getlicenseno())
    print("familycar - current speed - ", myfamilycar.getspeed())
    myluxarycar=familycar("LX1000", 80, 70,2)
    print("luxcar - license plate number - ", myluxarycar.getlicenseno())
    print("luxcar - current speed - ", myluxarycar.getspeed())
    mysportscar=sportscar("SP1000", 120, 90)
    print("sportscar - license plate number - ", mysportscar.getlicenseno())
    print("sportscar - current speed - ", mysportscar.getspeed())
    myluxarysportscar=luxarysportscar("LSP1000", 120, 90)
    print("luxarysportscar - license plate number - ", myluxarysportscar.getlicenseno())
    print("luxarysportscar - current speed - ", myluxarysportscar.getspeed())
