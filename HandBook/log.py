from datetime import datetime as dt

def Buses(data):
    time = dt.now().strftime("%H:%M")
    with open("log.txt", "a",encoding="utf-8") as file:
        file.write("{}, Buses, {}".format(time, data))
        
def Conductors(data):
    time = dt.now().strftime("%H:%M")
    with open("log.txt", "a",encoding="utf-8") as file:
        file.write("{}, Conductors, {}".format(time, data))
        
def Drivers(data):
    time = dt.now().strftime("%H:%M")
    with open("log.txt", "a",encoding="utf-8") as file:
        file.write("{}, Drivers, {}".format(time, data))
        
def PTI(data):
    time = dt.now().strftime("%H:%M")
    with open("log.txt", "a",encoding="utf-8") as file:
        file.write("{}, Passing a technical inspection, {}".format(time, data))
        
def TTIW(data):
    time = dt.now().strftime("%H:%M")
    with open("log.txt", "a",encoding="utf-8") as file:
        file.write("{}, Types of technical inspection works, {}".format(time, data))