from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    A Vehicle that has many attributes as well as functionalities that a real car may have.
    """
    def __init__(self, name, wheel_count = 4):
        """
        Initializes the Vehicle and sets the attributes
        """
        self.name = name
        self.wheel_count = wheel_count
        self.__fuel_level = 0
        self.__distance_travelled = 0
        self.__last_inspection = 0
    
    @property
    def name(self):
        """
        getter method for name
        """
        return self.__name
    
    @name.setter
    def name(self, name):
        """
        setter method for name
        """
        self.__name = name

    @property
    def wheel_count(self):
        """
        getter method for  no of wheels of vehicle
        """
        return self.__wheel_count
    
    @wheel_count.setter
    def wheel_count(self, wheel_count):
        """
        setter method for  no of wheels of vehicle
        """
        self.__wheel_count = wheel_count

    @staticmethod
    def is_oldtimer(first_reg):
        """
        checks is vehilce is older than 30 year before 2020
        """
        if 2020 - first_reg > 30:
            return True
        else:
            return False

    def drive(self, distance):
        """
        Drive the vehicle when a distance is provided.
        Increase distance covered and reduce the amount of fuel used.
        Refuel if fuel finishes
        """
        fuel_req = distance / 10 # Calculates fuel used(10km traveled means 1 liter fuel used)
        while distance != 0:
            if fuel_req > self.__fuel_level:
                self.__distance_travelled += self.__fuel_level * 10
                distance -= self.__fuel_level * 10
                fuel_req -= self.__fuel_level
                self.refuel()
            else:
                self.__fuel_level -= fuel_req # Decreases the fuel used
                self.__distance_travelled += distance
                distance = 0
        print("----Drive completed----")

    @abstractmethod
    def honk(self):
        """
        Honk 'tut tut'.
        method used in sub-class
        """
        pass

    def refuel(self, new_fuel = 100):
        """
        refuels the vehicle
        """
        self.__fuel_level += new_fuel # Tank has unlimited capacity
        print("----Tank refueled----")

    def need_inspection(self):
        """
        Calls inspection method when inspection needed
        """
        if self.__distance_travelled - self.__last_inspection > 1000:
            self.do_inspection()

    def do_inspection(self):
        """
        Does vehicle inspection and stores distance covered till inspection
        """
        self.__last_inspection = self.__distance_travelled
        print("----Vehicle inspection completed----")

    def obd(self):
        """
        Prints all vehicle data in organized manner
        """
        a = format(self.__fuel_level, '.2f')
        b = format(self.__distance_travelled, '.2f')
        return (print(f"\nVehicle:            {self.__name}\n" + 
        f"No. of wheels:      {self.__wheel_count}\n" + 
        f"Current fuel level: {a} liters\n" + 
        f"Distance travelled: {b}km\n" + 
        f"Last inspection   : {b}km"))
    
    def create_string(self):
        """
        Returns a string of all vehicle data to by printed using magic function
        """
        a = format(self.__fuel_level, '.2f')
        b = format(self.__distance_travelled, '.2f')
        return (f"\nVehicle:            {self.__name}\n" + 
        f"No. of wheels:      {self.__wheel_count}\n" + 
        f"Current fuel level: {a} liters\n" + 
        f"Distance travelled: {b}km\n" + 
        f"Last inspection   : {b}km")

    def __str__(self):
        """
        magic function to create string
        """
        return self.create_string()
    
    def __add__(self, other):
        """
        + operator magic function to add(crash) two wehicles.
        """
        sum = self.__wheel_count + other.__wheel_count
        print("There was a crash!")
        return sum
    
class clear_the_way(Vehicle):
    """
    child class defining vehicle honk
    """
    def honk(self):
        """
        prints the vehicle honk
        """
        print("Tut tut")