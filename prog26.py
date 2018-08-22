import this

class Car():
    total_num=0
    def __init__(self,make,model,year):
        Car.total_num+=1
        self.make=make
        self.model=model
        self.year=year

    def display_info(self):
        print('make is',self.make)
        print('model is',self.model)
        print('year of manufacture is',self.year)
        print('total number of cars are:',Car.total_num)

car1=Car('toyota','g class',2030)
car2=Car('mercedes','g-wagon',2013)
car1.display_info()
