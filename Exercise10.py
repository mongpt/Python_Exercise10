
#10.1
class Elevator:
    def __init__(self, botFloor, topFloor):
        self.botFloor = botFloor
        self.topFloor = topFloor

    def go_to_floor(self, floorNum):
        if floorNum <= self.topFloor:
            self.floor_up(floorNum)
            self.floor_down(floorNum)
        else:
            print(f"Please select floor again from {self.botFloor} to {self.topFloor}")

    def floor_up(self, floorNum):
        for i in range(self.botFloor, floorNum+1):
            print("Current Floor:", i)

    def floor_down(self, floorNum):
        for i in range(floorNum-1, self.botFloor-1, -1):
            print("Current Floor:", i)

print("\n****** Exercise 10.1 ******")
h = Elevator(1,10)
h.go_to_floor(5)

#10.2
class Elevator:
    def __init__(self, botFloor, topFloor):
        self.botFloor = botFloor
        self.topFloor = topFloor

    def go_to_floor(self, floorNum):
        if floorNum <= self.topFloor:
            self.floor_up(floorNum)
            self.floor_down(floorNum)
        else:
            print(f"Please select floor again from {self.botFloor} to {self.topFloor}")

    def floor_up(self, floorNum):
        for i in range(self.botFloor, floorNum+1):
            print("Current Floor:", i)

    def floor_down(self, floorNum):
        for i in range(floorNum-1, self.botFloor-1, -1):
            print("Current Floor:", i)

class Building:
    def __init__(self, numElevators, botFloor, topFloor):
        self.numElevators = numElevators
        self.elevatorNum = []
        self.botFloor = botFloor
        self.topFloor = topFloor
        for i in range(self.numElevators):
            self.elevatorNum.append(Elevator(self.botFloor, self.topFloor))

    def run_elevator(self, elevatorNum, destFloor):
        print(f"\nCurrent elevator: {elevatorNum}")
        self.elevatorNum[elevatorNum-1].floor_up(destFloor)


print("\n****** Exercise 10.2 ******")
b = Building(3, 0, 10)
b.run_elevator(1, 5)
b.run_elevator(2, 7)
b.run_elevator(3, 10)


#10.3
class Elevator:
    def __init__(self, botFloor, topFloor):
        self.botFloor = botFloor
        self.topFloor = topFloor

    def go_to_floor(self, floorNum):
        if floorNum <= self.topFloor:
            self.floor_up(floorNum)
            self.floor_down(floorNum)
        else:
            print(f"Please select floor again from {self.botFloor} to {self.topFloor}")

    def floor_up(self, floorNum):
        for i in range(self.botFloor, floorNum+1):
            print("Current Floor:", i)

    def floor_down(self, floorNum):
        for i in range(floorNum-1, self.botFloor-1, -1):
            print("Current Floor:", i)

class Building:
    def __init__(self, numElevators, botFloor, topFloor):
        self.numElevators = numElevators
        self.elevatorNum = []
        self.botFloor = botFloor
        self.topFloor = topFloor
        self.destFloor = []
        for i in range(self.numElevators):
            self.elevatorNum.append(Elevator(self.botFloor, self.topFloor))
            self.destFloor.append(self.botFloor)

    def run_elevator(self, elevatorNum, destFloor):
        self.destFloor[elevatorNum-1] = destFloor
        print(f"\nCurrent elevator: {elevatorNum}")
        self.elevatorNum[elevatorNum-1].floor_up(destFloor)

    def fire_alarm(self):
        print("\nFIRE!!!")
        for i in range(self.numElevators):
            print(f"\nElevator {i+1} is going down")
            self.elevatorNum[i].floor_down(self.destFloor[i]+1)


print("\n****** Exercise 10.3 ******")
b = Building(3, 0, 10)
b.run_elevator(1, 5)
b.run_elevator(2, 7)
b.run_elevator(3, 10)
b.fire_alarm()


#10.4
import random
from tabulate import tabulate


class car:
    def __init__(self, regNumber, maxSpeed):
        self.regNum = regNumber
        self.maxSpeed = maxSpeed
        self.curSpeed = 0
        self.travelledDistance = 0
        self.carStatus = {}

    def info(self):
        self.carStatus = {
            "Registration Number": self.regNum,
            "Maximum speed": self.maxSpeed,
            "Current speed": self.curSpeed,
            "Travelled Distance": self.travelledDistance
        }

    def accelerate(self, speed):
        self.curSpeed += speed
        if self.curSpeed < 0:
            self.curSpeed = 0
        elif self.curSpeed > self.maxSpeed:
            self.curSpeed = self.maxSpeed
        return self.curSpeed

    def drive(self, hours):
        self.travelledDistance += self.curSpeed * hours
        return self.travelledDistance


class Race:
    def __init__(self, name, distance, carList):
        self.name = name
        self.distance = distance
        self.carList = carList
        print("\nWelcome to Grand Demolition Derby car race")

    def hour_passes(self):
        for i in range(10):
            self.carList[i].accelerate(random.randint(-10, 15))
            self.carList[i].drive(1)
            self.carList[i].info()

    def print_status(self):
        raceResult = []
        for i in range(10):
            raceResult.append(self.carList[i].carStatus)
        print(tabulate(raceResult, headers="keys"))

    def race_finished(self):
        for c in self.carList:
            if c.travelledDistance >= self.distance:
                return True


print("\n****** Exercise 10.4 ******")
newCarList = []
for x in range(1, 11):
    newCar = car("ABC-" + str(x), random.randint(100, 200))
    newCarList.append(newCar)
newRace = Race("Grand Demolition Derby", 8000, newCarList)
hours = 0
while not newRace.race_finished():
    for x in range(10):
        hours += 1
        newRace.hour_passes()
        newRace.race_finished()
        if newRace.race_finished():
            break
    print(f"\nRace status after {hours} hours:")
    newRace.print_status()
print("\nFinal race result:")
newRace.print_status()

