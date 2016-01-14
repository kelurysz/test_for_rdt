
# class for passengers
class Person:
    def __init__(self, name = None, leave = None, arrive = None, status = False, busnum = None) :
        self.name = name
        self.leave = leave
        self.arrive = arrive
        self.status = status
        self.busnum = busnum # which bus the passenger is on

    def boardSuccess(self):
        '''
        see if passenger board successfully
        :return:
        '''
        self.status = True
    def getName(self):
        return self.name
    def getLeave(self):
        return self.leave
    def getArrive(self):
        return self.arrive
    def getRoute(self):
        return [self.getLeave(), self.getArrive()]
    def getStatus(self):
        return self.status
    def getBusnum(self):
        return self.busnum

    def setBusnum(self, num):
        self.busnum = num

    def __str__(self): # print the information of the passenger
                       # if he/she is waiting for a bus, tell users that he/she is waiting
                       # else, print the bus he/she's on
        tmp = "Passenger's name ... " + self.getName() + " ... now he/she is in ... " + self.getLeave() + \
                " ... and is going to ... " + self.getArrive()
        if self.getStatus() == False:
            tmp += ' ... now is waiting for a bus.'
        elif self.getStatus() == True:
            tmp += ' ... now is on No.' + self.getBusnum() + ' bus.'
        return tmp
