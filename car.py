class Car(object):
    
    def __init__(self, name="General", model="GM",car_type="saloon", speed=0):
        self.car_type = car_type
        self.name = name
        self.model = model
        self.speed = speed
        self.num_of_wheels = 4

        if self.name == "Porshe" or self.name == "Koenigsegg":
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if self.car_type == "trailer":
            self.num_of_wheels = 8
            self.speed = 0

    def is_saloon(self):
        if self.car_type != "trailer":
            return True
        else:
            return False
    def drive(self, speed):
        if self.car_type != "trailer":
            self.speed = 10**speed
        else:
            self.speed = 77
        return self