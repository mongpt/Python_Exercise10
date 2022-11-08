# Python_Exercise10
## 10. Association

1. Write an `Elevator` class that receives the numbers of the bottom and top floors as initializer parameters. The elevator has methods `go_to_floor`,
`floor_up` and `floor_down`. A new elevator is always at the bottom floor. If you make elevator `h` for example the method call `h.go_to_floor(5)`, the
method calls either the `floor_up` or `floor_down` methods as many times as it needs to get to the fifth floor. The methods run the elevator
one floor up or down and tell what floor the elevator is after each move. Test the class by creating an elevator in the main program, tell it to move
to a floor of your choice and then back to the bottom floor.
```python
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

h = Elevator(1,10)
h.go_to_floor(5)
```
Output console:
```
Current Floor: 1
Current Floor: 2
Current Floor: 3
Current Floor: 4
Current Floor: 5
Current Floor: 4
Current Floor: 3
Current Floor: 2
Current Floor: 1
```
2. Extend the previous program by creating a `Building` class. The initializer parameters for the class are the numbers of the bottom and top floors and
the number of elevators in the building. When a building is created, the building creates the required number of elevators. The list of elevators is 
stored as a property of the building. Write a method called `run_elevator` that accepts the number of the elevator and the destination floor as its
parameters. In the main program, write the statements for creating a new building and running the elevators of the building.
```python
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


b = Building(3, 0, 10)
b.run_elevator(1, 5)
b.run_elevator(2, 7)
b.run_elevator(3, 10)
```
Output console:
```
Current elevator: 1
Current Floor: 0
Current Floor: 1
Current Floor: 2
Current Floor: 3
Current Floor: 4
Current Floor: 5

Current elevator: 2
Current Floor: 0
Current Floor: 1
Current Floor: 2
Current Floor: 3
Current Floor: 4
Current Floor: 5
Current Floor: 6
Current Floor: 7

Current elevator: 3
Current Floor: 0
Current Floor: 1
Current Floor: 2
Current Floor: 3
Current Floor: 4
Current Floor: 5
Current Floor: 6
Current Floor: 7
Current Floor: 8
Current Floor: 9
Current Floor: 10
```
3. Extend the program again by adding a method `fire_alarm` that does not receive any parameters and moves all elevators to the bottom floor. Continue 
the main program by causing a fire alarm in your building.
```python
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


b = Building(3, 0, 10)
b.run_elevator(1, 5)
b.run_elevator(2, 7)
b.run_elevator(3, 10)
b.fire_alarm()
```
Output console:
```
Current elevator: 1
Current Floor: 0
Current Floor: 1
Current Floor: 2
Current Floor: 3
Current Floor: 4
Current Floor: 5

Current elevator: 2
Current Floor: 0
Current Floor: 1
Current Floor: 2
Current Floor: 3
Current Floor: 4
Current Floor: 5
Current Floor: 6
Current Floor: 7

Current elevator: 3
Current Floor: 0
Current Floor: 1
Current Floor: 2
Current Floor: 3
Current Floor: 4
Current Floor: 5
Current Floor: 6
Current Floor: 7
Current Floor: 8
Current Floor: 9
Current Floor: 10

FIRE!!!

Elevator 1 is going down
Current Floor: 5
Current Floor: 4
Current Floor: 3
Current Floor: 2
Current Floor: 1
Current Floor: 0

Elevator 2 is going down
Current Floor: 7
Current Floor: 6
Current Floor: 5
Current Floor: 4
Current Floor: 3
Current Floor: 2
Current Floor: 1
Current Floor: 0

Elevator 3 is going down
Current Floor: 10
Current Floor: 9
Current Floor: 8
Current Floor: 7
Current Floor: 6
Current Floor: 5
Current Floor: 4
Current Floor: 3
Current Floor: 2
Current Floor: 1
Current Floor: 0
```
4. This exercise continues the previous car race exercise from the last exercise set. Write a `Race` class that has the following properties:
name, distance in kilometers and a list of cars participating in the race. The class has an initializer that receives the name, kilometers, and car list 
as parameters and sets their values to the corresponding properties in the class. The class has the following methods:
   - `hour_passes`, which performs the operations done once per hour in the original exercise: generates a random change of speed for each car and calls 
   their `drive` method.
   - `print_status`, which prints out the current information of each car as a clear, formatted table.
   - `race_finished`, which returns `True` if any of the cars has reached the finish line, meaning that they have driven the entire distance of the race.

   Write a main program that creates an 8000-kilometer race called `Grand Demolition Derby`. The new race is given a list of ten cars similarly to the
   earlier exercise. The main program simulates the progressing of the race by calling the `hour_passes` in a loop, after which it uses the `race_finished`
   method to check if the race has finished. The current status is printed out using the `print_status` method every ten hours and then once more at the
   end of the race.
```python
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
```
Output console:
```
****** Exercise 10.4 ******

Welcome to Grand Demolition Derby car race

Race status after 10 hours:
Registration Number      Maximum speed    Current speed    Travelled Distance
---------------------  ---------------  ---------------  --------------------
ABC-1                              116               12                    25
ABC-2                              200               70                   411
ABC-3                              170               44                   235
ABC-4                              154               29                   156
ABC-5                              107               32                   155
ABC-6                              187               33                   167
ABC-7                              176               38                   301
ABC-8                              182               10                   115
ABC-9                              175               33                   338
ABC-10                             114                0                    15

Race status after 20 hours:
Registration Number      Maximum speed    Current speed    Travelled Distance
---------------------  ---------------  ---------------  --------------------
ABC-1                              116               69                   478
ABC-2                              200              110                  1404
ABC-3                              170               81                   939
ABC-4                              154               34                   346
ABC-5                              107               28                   477
ABC-6                              187               77                   790
ABC-7                              176               83                   938
ABC-8                              182               35                   370
ABC-9                              175               36                   697
ABC-10                             114               30                   359

Race status after 30 hours:
Registration Number      Maximum speed    Current speed    Travelled Distance
---------------------  ---------------  ---------------  --------------------
ABC-1                              116               73                  1194
ABC-2                              200              148                  2776
ABC-3                              170               86                  1859
ABC-4                              154               94                  1100
ABC-5                              107              107                  1213
ABC-6                              187               86                  1636
ABC-7                              176              111                  1924
ABC-8                              182               74                   969
ABC-9                              175               90                  1267
ABC-10                             114               74                   915

Race status after 40 hours:
Registration Number      Maximum speed    Current speed    Travelled Distance
---------------------  ---------------  ---------------  --------------------
ABC-1                              116              116                  2148
ABC-2                              200              189                  4527
ABC-3                              170               76                  2770
ABC-4                              154              108                  2156
ABC-5                              107               98                  2234
ABC-6                              187              108                  2571
ABC-7                              176              129                  3130
ABC-8                              182               77                  1744
ABC-9                              175              120                  2434
ABC-10                             114               83                  1687

Race status after 50 hours:
Registration Number      Maximum speed    Current speed    Travelled Distance
---------------------  ---------------  ---------------  --------------------
ABC-1                              116              114                  3283
ABC-2                              200              200                  6438
ABC-3                              170              106                  3688
ABC-4                              154              105                  3300
ABC-5                              107              105                  3172
ABC-6                              187              114                  3719
ABC-7                              176              135                  4568
ABC-8                              182               75                  2487
ABC-9                              175              121                  3583
ABC-10                             114              113                  2759

Race status after 58 hours:
Registration Number      Maximum speed    Current speed    Travelled Distance
---------------------  ---------------  ---------------  --------------------
ABC-1                              116              116                  4209
ABC-2                              200              197                  8000
ABC-3                              170              136                  4782
ABC-4                              154              133                  4264
ABC-5                              107              100                  4008
ABC-6                              187              154                  4844
ABC-7                              176              174                  5834
ABC-8                              182              111                  3291
ABC-9                              175              152                  4766
ABC-10                             114              105                  3625

Final race result:
Registration Number      Maximum speed    Current speed    Travelled Distance
---------------------  ---------------  ---------------  --------------------
ABC-1                              116              116                  4209
ABC-2                              200              197                  8000
ABC-3                              170              136                  4782
ABC-4                              154              133                  4264
ABC-5                              107              100                  4008
ABC-6                              187              154                  4844
ABC-7                              176              174                  5834
ABC-8                              182              111                  3291
ABC-9                              175              152                  4766
ABC-10                             114              105                  3625
```
