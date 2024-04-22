class Vehicle():
    def __init__(self, name, wheel_count = 4): # I gave them initial values because the test provided in the exercise sheet did not set attribute values for this class.
        self.name = name
        self.wheel_count = wheel_count
        self.fuel_level = 0
        self.distance_travelled = 0
        self.last_inspection = 0

        # Error handling
        # No. of wheels should be positive integer
        try:
            is_integer = int(str(wheel_count))
        except ValueError:
            print("Error: Number of wheels should be an integer.")
            exit()
        # No. of wheels must be more than 0
        if wheel_count < 0:
            print("Error: Number of wheels should be a positive integer.")
            exit()
            
    def drive(self, distance):

        # Error handling
        # Distance should be positive number
        try:
            is_number = float(distance)
        except ValueError:
            print("Error: Distance must be a number")
            exit()
        # Distance must not be negative
        if distance < 0:
            print("Error: Distance should be a positive number.")
            exit()

        fuel_req = distance / 10 # Calculates fuel used(10km traveled means 1 liter fuel used)
        while distance != 0:
            if fuel_req > self.fuel_level:
                self.distance_travelled += self.fuel_level * 10
                distance -= self.fuel_level * 10
                fuel_req -= self.fuel_level
                self.refuel()
            else:
                self.fuel_level -= fuel_req # Decreases the fuel used
                self.distance_travelled += distance
                distance = 0
        print("----Drive completed----")

    def honk(self):
        print("Tut tut")

    def refuel(self, new_fuel = 100):

        # Error handling
        # Fuel amount should be positive number
        try:
            is_number = float(new_fuel)
        except ValueError:
            print("Erros: Amount of fuel must be a number")
            exit()
        # Distance must not be negative
        if new_fuel < 0:
            print("Error: Amount of fuel should be a positive number.")
            exit()

        self.fuel_level += new_fuel # Tank has unlimited capacity
        print("----Tank refueled----")

    def need_inspection(self):
        if self.distance_travelled - self.last_inspection > 1000:
            self.do_inspection()

    def do_inspection(self):
        self.last_inspection = self.distance_travelled
        print("----Vehicle inspection completed----")

    def obd(self):
        a = format(self.fuel_level, '.2f')
        b = format(self.distance_travelled, '.2f')
        print(f"\nVehicle:            {self.name}")
        print(f"No. of wheels:      {self.wheel_count}")
        print(f"Current fuel level: {a} liters")
        print(f"Distance travelled: {b}km")
        print(f"Last inspection   : {b}km")

# Test cases ------
BMW = Vehicle("M1", 4)
#BMW = Vehicle("M1", 4.5)
#BMW = Vehicle("M1", -5)
#BMW.drive(120)
#BMW.drive(-120)
#BMW.drive("abc")
#BMW.refuel("abc")
#BMW.refuel(-20)
#BMW.refuel(20)