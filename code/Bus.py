# class for buses
class Bus:
    def __init__(self, bus_number = None, leave=None, arrive=None, load = '0', status = 'Available'):
        self.number = bus_number
        self.load = load
        self.leave = leave
        self.arrive = arrive
        self.route = [leave, arrive]
        self.status = status

    def isFull(self):   # to check if the bus is full.
                        # I set one bus can contain 100 people at the same time.
        if int(self.load) >= 100:
            return True
        else:
            return False
    def changeStatus(self): # change the status of a bus. whether it is full or not.
        if self.isFull():
            self.status = 'Full'
    def swapL_A(self): # swap the bus' departure and destination
        arrive = self.getLeave()
        leave = self.getArrive()
        self.setArrive(arrive)
        self.setLeave(leave)
    def addPerson(self, person): # add one passenger to the bus
        tmp = int(self.load) + 1
        self.load = str(tmp)
        self.changeStatus()
    def afterOneTrip(self): # after one trip, swap the departure and destination, reset the route
                            # and clear the passengers
        self.swapL_A()
        self.setRoute()
        self.clearLoad()

    def getNumber(self):
        return str(self.number)
    def getArrive(self):
        return str(self.route[1])
    def getLeave(self):
        return str(self.route[0])
    def getLoad(self):
        return str(self.load)
    def getRoute(self):
        return [self.getLeave(), self.getArrive()]
    def getStatus(self):
        return self.status
    def clearLoad(self):
        self.load = '0'
        self.status = 'Available'
        # self.person.clear()

    def setRoute(self):
        self.route = [self.getLeave(), self.getArrive()]
    def setLeave(self, leave):
        self.route[0] = leave
    def setArrive(self, arrive):
        self.route[1] = arrive

    def oneOffboard(self): # if one passenger decide to get off the bus
        temp = int(self.getLoad()) - 1
        self.load = str(temp)

    def __str__(self): # print the bus' information
        temp = "The bus No." + str(self.number) + ", comes from ... " \
               + self.getLeave() + ", arrives at ... " + self.getArrive()
        if self.isFull():
            temp += "\n\tnow is FULL!"
        else:
            temp += "\n\tnow has " + str(100 - int(self.load)) + " seat(s) available."
        return temp