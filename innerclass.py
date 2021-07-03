
class Student:

    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.age)
        self.lap.show()

    class Laptop:

        def __init__(self):
            self.cpu = "cpu"
            self.ram =  4

        def show(self):
            print(self.cpu, self.ram)



s1 = Student("Tareq","25")
s1.lap.cpu = "i5"
s1.lap.ram = 8
s1.show()