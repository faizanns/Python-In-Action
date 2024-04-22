#Vehicle class
class Vehicle():
    def __init__(self, name, wheel_count = 4): # I gave them initial values because the test provided in the exercise sheet did not set attribute values for this class.
        self.name = name
        self.wheel_count = wheel_count
        self.fuel_level = 0
        self.distance_travelled = 0
        self.last_inspection = 0

    def drive(self, distance):
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



#Question 1
#Car
class Car(Vehicle):
    def __init__(self, name, max_speed, passenger_count = 0):
        self.passenger_count = passenger_count
        self.max_speed = max_speed
        super().__init__(name)

    def get_in(self, persons_to_move): # new get_in method introduced that enters people in car if possible
        if persons_to_move + self.passenger_count <= 5:
            print(f"{persons_to_move} person(s) got in the car.")
            self.passenger_count += persons_to_move
        else:
            print(f"Not enough place for {persons_to_move} person(s).")
            print(f"{self.passenger_count + persons_to_move - 5} person(s) have to to get out first.")

#Audi
class Audi(Car):
    def __init__(self, *car_args):
        super().__init__(*car_args) # constructor NOT overwritten

    def obd(self): # method obd overwritten
        print(f"This is an Audi {self.name} with max speed of {self.max_speed}km/h.")
        return None

#BMW    
class BMW(Car):
    def __init__(self, *car_args):
        super().__init__(*car_args) # constructor NOT overwritten

    def obd(self): # method obd overwritten
        print(f"This is a BMW {self.name} with max speed of {self.max_speed}km/h.")
        a = format(self.fuel_level, '.2f')
        b = format(self.distance_travelled, '.2f')
        print(f"No. of wheels:      {self.wheel_count}")
        print(f"Current fuel level: {a} liters")
        print(f"Distance travelled: {b}km")
        print(f"Passengers:         {self.passenger_count}\n")
    
    def online_inspection(self):
        self.do_inspection()


#Tests start -------------
audi_car = Audi("A3", 320)
audi_car.obd()
bmw_car = BMW("M6", 340)
bmw_car.obd()

print(str(bmw_car.fuel_level) + " liters") # fuel level before refuel
bmw_car.refuel(100)
print(str(bmw_car.fuel_level) + " liters\n") # fuel level after refuel


print(str(bmw_car.distance_travelled) + "km travelled") # distance travelled before drive
bmw_car.drive(200)
print(str(bmw_car.distance_travelled) + "km travelled\n") # distance travelled after drive

bmw_car.obd()
bmw_car.get_in(4)

bmw_car.online_inspection()
bmw_car.obd()
# Tests end -------------



# Question 2
# Truck
class Truck(Vehicle):
    def __init__(self, name, max_vol = 80, *vehicle_args):
        super().__init__(name, *vehicle_args)
        self.wheel_count = 10 # constructor of class Vehicle overwritten
        self.packages = []
        self.max_vol = max_vol

    def load(self, new_packages = []):
        current_vol = 0
        for i in self.packages: # calculates volume of packages already stored
            current_vol += i
        loaded = []
        if current_vol != self.max_vol:
            for i in range(len(new_packages)): # checks if new packages can be added and adds new packages
                if self.max_vol >= current_vol + new_packages[i]:
                    current_vol += new_packages[i]
                    self.packages.append(new_packages[i])
                    loaded.append(new_packages[i])
            if len(loaded) == 0:
                print("None of the packages could be loaded. Not enough space.")
            elif len(loaded) == len(new_packages):
                print("All packages loaded")
            else:
                print(f"Limited space. only these packages loaded: {loaded}")
        else:
            print("Truck is already full!")

    def unload(self, x): # unload first x packages
        if len(self.packages) <= x:
            self.packages = []
        else:
            for i in range(x):
                del self.packages[0]

    def obd(self): # Method obd overwritten so that it displays load
        a = format(self.fuel_level, '.2f')
        b = format(self.distance_travelled, '.2f')
        print(f"Vehicle:            {self.name}")
        print(f"No. of wheels:      {self.wheel_count}")
        print(f"Max capacity:       {self.max_vol}")
        print(f"Current load:       {self.packages}\n")

# Tests start -------                
man = Truck("MAN")
man.obd()
man.load([10, 24, 5, 34])
man.obd()
man.unload(2)
man.obd()
man.load([10, 24, 5, 34, 80])
man.obd()
man.unload(10)
man.obd()
# Tests end -------


#Question 3
class Pickup(Car, Truck):
    def __init__(self, name, max_speed, max_vol, *vehicle_args):
        Car.__init__(self, name, max_speed, *vehicle_args)
        Truck.__init__(self, name, max_vol, *vehicle_args)
        self.name = name
        self.max_speed = max_speed
        self.max_vol = max_vol

    def obd(self):
        a = format(self.fuel_level, '.2f')
        b = format(self.distance_travelled, '.2f')
        print(f"\nVehicle:            {self.name}")
        print(f"No. of wheels:      {self.wheel_count}")
        print(f"Max speed:          {self.max_speed}")
        print(f"Max capacity:       {self.max_vol}")
        print(f"Current fuel level: {a} liters")
        print(f"Distance travelled: {b}km")
        print(f"Current load:       {self.packages}")
        print(f"Passengers:         {self.passenger_count}\n")
    
    
# Tests start ------
ford = Pickup("F-150", 180, 25)
ford.refuel(130)
ford.get_in(3)
ford.drive(10000)
ford.load([2,5,11])
ford.obd()
# Tests end ------