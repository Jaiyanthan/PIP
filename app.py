class Car:
    def __init__(self, brand, price, maxSpeed):
        self.brand = brand
        self.price = price
        self.maxSpeed = maxSpeed

    def start(self):
         print(self.brand + " is started")

    def stop(self):
        print(self.brand + " is stopped")

## Creating a class object
RollsRoyce = Car("Rolls Royce", "13 crores", "250 kmph")        
RollsRoyce.start()