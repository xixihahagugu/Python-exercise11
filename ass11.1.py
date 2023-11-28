class Car:
    def __init__(self,registration_number,maximum_speed):
        self.registration_number=registration_number
        self.maximum_speed=maximum_speed
        self.current_speed=0
        self.travelled_distance=0

    def accelerate(self,change_speed):
        if 0<=(self.current_speed+change_speed)<=self.maximum_speed:
            self.current_speed += change_speed
    def drive(self,time):
        self.travelled_distance+=time*self.current_speed

class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed,capbattery):
        self.capbattery=capbattery
        super().__init__(registration_number, maximum_speed)

class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed,voltank):
        self.voltank=voltank
        super().__init__(registration_number, maximum_speed)

car15=ElectricCar("ABC-15", 180, 52.5)
car123=GasolineCar("ACD-123", 165, 32.3)
car15.accelerate(90)
car15.drive(3)
print(f"travelled distance:{car15.travelled_distance}km")
car123.accelerate(95)
car123.drive(3)
print(f"travelled distance:{car123.travelled_distance}km")