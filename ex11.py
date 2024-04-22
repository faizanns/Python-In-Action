def new_vehicle(name, fuel_level, distance_travelled, *wheel_count):
    Mercedes = Vehicle(name, fuel_level, distance_travelled, *wheel_count)
    for drives in range(6):
        if Mercedes.fuel_level < 2: # 2 liters of fuel or less is considered as empty tank
            Mercedes.refuel()

        distance = float(input("Enter distance to travel: "))
        Mercedes.drive(distance)
        
        if Mercedes.need_inspection() == True:
            Mercedes.do_inspection()
        
        if drives % 3 == 0:
            Mercedes.honk()

    Mercedes.obd()

class Vehicle():
    def __init__(self, name, fuel_level, distance_travelled, wheel_count = 4):
        self.name = name
        self.wheel_count = wheel_count
        self.fuel_level = fuel_level
        self.distance_travelled = distance_travelled

    def drive(self, distance):

        while (distance > self.fuel_level * 10):
            print("Not enough fuel!")
            distance = float(input("Enter smaller distance to travel: "))
        fuel_used = distance / 10 # Calculates fuel used(10km traveled means 1 liter fuel used)
        self.fuel_level -= fuel_used # Decreases the fuel used
        self.distance_travelled += distance

    def honk(self):
        print("Tut tut")

    def refuel(self):
        self.fuel_level = 71 # Tank capacity is 71 liters
        print("----Tank refilled----")

    def need_inspection(self):
        if self.distance_travelled >= 1000:
            return True
        else:
            return False

    def do_inspection(self):
        self.distance_travelled = 0
        print("----Vehicle inspection completed----")

    def obd(self):
        a = format(self.fuel_level, '.2f')
        b = format(self.distance_travelled, '.2f')
        print(f"\nVehicle:            {self.name}")
        print(f"No. of wheels:      {self.wheel_count}")
        print(f"Current fuel level: {a} liters")
        print(f"Distance travelled: {b}km")

new_vehicle("BMW", 24, 60, 4) # A BMW with 24 liters of fuel, 60km already travelled, and has 4 wheels.