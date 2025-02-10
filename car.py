class Car:
    def __init__(self,color,YOM,):
        self.color = color
        self.YOM = YOM

    def drive(self):
        print("You drive a",self.color,"car")

car1 = Car("black",2010)
print(car1.color)
car1.drive()
car2 = Car("blue",2009)
print(car2.color)
car2.drive()

