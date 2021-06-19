
class Car:    # Defining a class
    wheels = 4       # this is a class variable
    def __init__(self):  # Init method of the class car
        self.com = "Com" # this is an instance variable
        self.mil = 10     # this is an instance variable



c1 = Car()              # Creating an object c1 of class Car
c1.mil = 20             # this is an instance variable
c1.com = "Lamorghini"   # this is an instance variable
c2 = Car()              # Creating an object c2 of class Car
c2.mil = 15             # this is an instance variable
c2.com = "Ferrari"      # this is an instance variable

Car.wheels = 6  # Changes the class variable wheels value to 6 from 4

print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil,c1.wheels)