__author__ = "Shuzhi Yang(Susie)"
import os.path

# import sys, os
# sys.path.append('E:/Intern/mypackage')

from Station import Station
from Bus import Bus
from Person import Person
# import Station
# import Bus
# import Person

bus = []  # list to store buses
destinations = []  # list to store destinations(stations)
person = []  # list to store passengers

# check whether the number is already used as a bus numbers.
# if used, return true; if not, return false.

def bus_numberExist(bus, num):
    for item in bus:
        if item.getNumber() == num:
            print("Bus number already exists! Input again, please.")
            return True
    return False


# check whether the name is already used as a station name.
# if used, return true; if not, return false.
def station_nameExist(destinations, name):
    for item in destinations:
        if item.getName() == name:
            return True
    return False

# check the input is valid or not.
# no space in the front. Digits, characters and some marks are allowed.
def valid_input(str):
    if str[0] == ' ':
        print("No space in the front! Input again, please.")
        return False

    for i in range(len(str)):
        if '0' <= str[i] and '9' >= str[i]:
            if 'a' <= str[i] and 'z' >= str[i]:
                if 'A' <= str[i] and 'Z' >= str[i]:
                    if str[i] != '.' or str[i] != '-' or str[i] != '_':
                        print("Invalid input. Input again, please.")
                        return False
        return True


# register a new bus
def addBus(bus):
    print("Set the number of the bus:")
    num = input()
    while bus_numberExist(bus, num): # if the bus' number is already in use, input again
        num = input()

    print("The departure of the bus: ")
    depa = input()
    while not station_nameExist(destinations, depa): # the departure must be a station registered
                                                      # if not, input again
        print("Station doesn't exist! Input again, please.")
        depa = input()

    print("The destination of the bus:")
    dest = input()
    while depa == dest or not station_nameExist(destinations, dest): # the destination must be a station registered
                                                                      # if not, input again. And it should not be the same
                                                                      # station as its departure.
        if depa == dest:
            print("Destination is the same with departure! Input again, please.")
        if not station_nameExist(destinations, dest):
            print("Station doesn't exist! Input again, please.")
        dest = input()
    tmp = Bus(num, depa, dest)
    bus.append(tmp)
    print("Success!!")


# register a new station
def addStation(destinations):
    print("Set the name of the new station:")
    name = input()
    while station_nameExist(destinations, name) and not valid_input(name):
        # the station's name should not be the same with other station's name.
        # and its name should not be something weird.
        if station_nameExist(destinations, name):
            print("Station name already exists! Input again, please.")
        name = input()
    tmp = Station(name)
    destinations.append(tmp)
    print("Success!")


# add a new passenger, and find a seat for him/her.
# if no bus available, he/she will wait.
def addPerson(person):
    print("New passenger's name:")
    name = input()
    print("New passenger's departure:")
    dep = input()
    print("New passenger's destination:")
    des = input()
    while des == dep:
        print("Destination is the same with departure! Input again, please.")
        des = input()
    tmp = Person(name, dep, des)
    for item in bus:
        # find if there are any buses have seat available for this passenger
        if tmp.getRoute() == item.getRoute() and not item.isFull():
            tmp.boardSuccess()
            tmp.setBusnum(item.getNumber())
            item.addPerson(tmp)
            print("Board successfully!")
            person.append(tmp)
            return
    # if no seats availble:
    print("All bus full or your route is not availble! You have to wait.")
    person.append(tmp)

# see if there are anyone waiting can get on a bus
def tryBoardAgain(person, bus):
    '''
    see if there are anyone waiting can get on a bus

    :param person:
    :param bus:
    :return:
    '''
    flag = False # indicate whether if there are any changes in passengers' status
    for tmp in person:
        if tmp.getStatus() == False:
            for item in bus:
                if tmp.getRoute() == item.getRoute() and not item.isFull():
                    tmp.boardSuccess()
                    tmp.setBusnum(item.getNumber())
                    item.addPerson(tmp)
                    flag = True # if someone get on a bus
    if flag: # if passenger status changed
        print("Someone get on a bus finally! :P\n")
    else: # if not
        print("Still no new seat(s) availble. :(\n")


#
def print_des(destinations):
    '''
    print the information of destinations

    :param destinations: destination
    :return:

    '''
    for item in destinations:
        print(str(item))


# print the information of buses
def print_bus(bus):
    '''

    :param bus:
    :return:
    '''
    for item in bus:
        print(str(item))


# print the information of passengers
def print_person(person):
    '''
    print the information of passengers

    :param person:
    :return:
    '''
    for item in person:
        print(str(item))


#
def print_person_by_bus(person, bus):
    '''
    print passenger's information by the bus they take.

    :param person:
    :param bus:
    :return:
    '''
    for b in bus:
        busnum = b.getNumber() # get the bus number
        print("On No." + str(busnum) + ":")
        for p in person: # scan the person list, look for the same bus number
            if p.getBusnum() == busnum:
                print(p.getName()) # print passenger's name
    print("Passengers waiting:") # print passengers waiting for buses
    for p in person:
        if p.getStatus() == False:
            print(p.getName())
    print('\n')


#
def delBus(bus):
    '''
    delete a bus. If the bus is empty(load = 0), delete it.
    else, print a warning, and quit.

    :param bus:
    :return:
    '''
    print("Which BUS do you want to remove?")
    num = input()
    empty = True
    for item in range(len(bus)):
        if bus[item].getNumber() == num: # find the bus number
            if bus[item].getLoad() == '0': # if the bus is empty
                del bus[item]
                print("Success!")
                return
            empty = False
    if not empty:
        print("The bus is not empty!")
    else:
        print("The bus number doesn't exist.")


# delete a station. If the station is in use, quit the function.
def delStation(destinations, bus):
    print("Which STATION do you want to remove?")
    sta = input()
    for item in bus:
        if item.getArrive() == sta or item.getLeave() == sta: # if the station is in use
            print("The station is in use!")
            return
    for i in range(len(destinations)): # delete
        if destinations[i].getName() == sta:
            del destinations[i]
            return
    print("The station doesn't exist!")


# delete a passenger. If the passenger is on a bus, delete him/her from the bus, too.
def delPerson(person, bus):
    '''
    delete a passenger. If the passenger is on a bus, delete him/her from the bus, too.

    :param person:
    :param bus:
    :return:
    '''
    print("Which PASSENGER do you want to remove?")
    name = input()
    flag = False
    for i in range(len(person)):
        if person[i].getName() == name:
            flag = True
            if person[i].getStatus() == True: # if the person is on a bus
                for item in bus:
                    if item.getNumber() == person[i].getBusnum(): # find the bus number
                        item.oneOffboard() # decrease bus load)
                        del person[i]
                        return
            del person[i]
    if not flag:
        print("No such person.")


# start a trip and set the relevant information.
def afterOneTrip(bus, person):
    print("We have these buses:")
    print_bus(bus)
    print("Which bus should start the trip? 'all' for all buses.")
    num = input()
    if bus_numberExist(bus, num) and num != 'all':
        for item in range(len(person)):
            if person[item].getBusnum == num:
                del person[item]
        for item in bus:
            if item.getNumber == number:
                item.afterOneTrip()
    elif num == 'all':
        person.clear()
        for item in bus:
            item.afterOneTrip()
    print("Trip finished!\n")


#
def read_from_file(destinations, bus, person):
    '''
    read all the information from files
    :param destinations:
    :param bus:
    :param person:
    :return:
    '''
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'destination.txt')
    f = open(filename)
    lines = [line.rstrip('\n') for line in f]
    for item in lines:
        des = Station(item)
        destinations.append(des)
    del destinations[0]
    f.close()

    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'bus.txt')
    f = open(filename)
    lines = [line.rstrip('\n') for line in f]
    for item in lines:
        item = item.split('\t')
        pos = len(item) - 1
        tmp = Bus(item[0], item[2], item[4], item[pos - 2], item[pos])
        bus.append(tmp)
    del bus[0]
    f.close()

    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'person.txt')
    f = open(filename)
    lines = [line.rstrip('\n') for line in f]
    for item in lines:
        item = item.split('\t')
        end = len(item) - 1
        status = False
        if item[end - 2] == 'Onboard':
            status = True
        num = item[end]
        if num == 'None':
            num = None
        else:
            num = str(num)
        tmp = Person(item[0], item[1], item[3], status, num)
        person.append(tmp)
    del person[0]
    f.close()


#
def save_to_file(destinations, bus, person):
    '''
    save all the information to files

    :param destinations:
    :param bus:
    :param person:
    :return:
    '''
    f = open('destination.txt', 'w')
    f.write("Destination Names:\n")
    for item in destinations:
        f.write(item.getName() + '\n')
    f.close()

    f = open('bus.txt', 'w')
    f.write("Bus No.\t\tDeparture\tDestination\tCurrent Load\tStatus\n")
    for item in bus:
        f.write(item.getNumber() + '\t\t' + item.getLeave() + '\t\t' + item.getArrive() + \
                '\t\t' + item.getLoad() + '\t\t' + item.getStatus() + '\n')
    f.close()

    f = open('person.txt', 'w')
    f.write("Name:\t\tDeparture:\tDestination:\tStatus\t\tBus No.\n")
    for item in person:
        f.write(item.getName() + '\t' + item.getLeave() + '\t\t' + item.getArrive())
        if item.getStatus() == True:
            f.write('\t\t' + 'Onboard')
        elif item.getStatus() == False:
            f.write('\t\t' + 'Waiting')
        if item.getBusnum() != None:
            f.write('\t\t' + item.getBusnum() + '\n')
        else:
            f.write('\t\t' + 'None' + '\n')
    f.close()

###############################################
#########          MENU           #############
###############################################

print("Welcome to YSZ's bus company!")
read_from_file(destinations, bus, person)
menu = "WHAT DO YOU WANT TO DO:\n" + \
      "press 1 to ADD new buses/stations/passengers\n" + \
      "press 2 to DELETE buses/stations/passengers\n" + \
      "press 3 to START a trip\n" + \
      "press 4 to check if anyone waiting can get on a bus.\n" + \
      "press 5 to see who is on which bus.\n" + \
      "press 6 to see all the current information.\n" + \
      "press 0 to save the status and quit the program."
print(menu)
choice = int(input())
while choice != 0:

    # choose to add
    if choice == 1:
        print("What do you want to ADD?\n"
              "1: station(s)\t2:bus(es)\t3:passenger(s)\t0:quit")
        choice1 = int(input())
        while choice1 != 0:
            # choose to add station(s)
            if choice1 == 1:
                print("We have these stations:")
                print_des(destinations)
                print("How many STATIONS do you want to add? 0 to quit.")
                number = int(input())
                for count in range(number):
                    addStation(destinations)
            # choose to add bus(es)
            elif choice1 == 2:
                print("We have these buses:")
                print_bus(bus)
                print("How many BUS do you want to add? 0 to quit.")
                number = int(input())
                for count in range(number):
                    addBus(bus)
            # choose to add person(s)
            elif choice1 == 3:
                print("We have these passengers:")
                print_person(person)
                print("How many PEOPLE do you want to add?  0 to quit.")
                number = int(input())
                for count in range(number):
                    addPerson(person)
            elif choice1 != 0:
                print("No such choice. Input again, please.")
            print("press 0 to quit.")
            choice1 = int(input())

    # choose to delete
    elif choice == 2:
        print("What do you want to DELETE?\n"
              "1: station(s)\t2:bus(es)\t3:passenger(s)\t0:quit")
        choice1 = int(input())
        while choice1 != 0:
            # choose to delete station(s)
            if choice1 == 1:
                print_des(destinations)
                print("How many STATIONS do you want to delete? 0 to quit.")
                number = int(input())
                for count in range(number):
                    delStation(destinations, bus)
                    print("Now we have these stations:")
                    print_des(destinations)
            # choose to delete bus(es)
            elif choice1 == 2:
                print_bus(bus)
                print("How many BUS do you want to delete? 0 to quit.")
                number = int(input())
                for count in range(number):
                    delBus(bus)
                    print("Now we have bus(es):")
                    print_bus(bus)
            # choose to delete person(s)
            elif choice1 == 3:
                print_person(person)
                print("How many PEOPLE do you want to delete? 0 to quit.")
                number = int(input())
                for count in range(number):
                    delPerson(person, bus)
                    print("Now we have passenger(s):")
                    print_person(person)
            elif choice1 != 0:
                print("No such choice. Input again, please.")
            print("press 0 to quit.")
            choice1 = int(input())

    # choose to start a trip
    elif choice == 3:
        afterOneTrip(bus, person)

    # choose to check if anyone waiting can get on a bus
    elif choice == 4:
        tryBoardAgain(person, bus)

    # choose to print person by bus
    elif choice == 5:
        print_person_by_bus(person, bus)

    # choose to print all the current information
    elif choice == 6:
        print("We have these stations:")
        print_des(destinations)
        print("\nWe have these buses:")
        print_bus(bus)
        print("\nWe have these passengers:")
        print_person(person)

    # if the input is not included in the menu:
    else:
        print("Wrong option. Input again, please.")

    # if user didn't choose to quit
    if choice != 0:
        print(menu)
        choice = int(input())

save_to_file(destinations, bus, person)
print("File saved. Bye.")