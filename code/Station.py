# class for stations
class Station:
    station_count = 0
    def __init__(self, name):
        self.name = name
        self.stationnum = str(Station.station_count)
        Station.station_count += 1

    def getName(self):
        return self.name

    def __str__(self):
        tmp = "The No." + self.stationnum + " station's name is: " + self.name
        return tmp