class Car(object):
    
    def __init__(self, car_type="saloon", name="General", model="GM", speed=0):
        self.car_type = car_type
        self.name = name
        self.model = model
        self.speed = speed

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