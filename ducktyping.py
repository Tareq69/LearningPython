

class Pycharm:
    def execute(self):
        print('Compiling')
        print("Running")


class Intellij:
    def execute(self):
        print('Checking')
        print("Testing")
        print('Compiling')
        print("Running")

class Laptop:

    def code(self,ide):
        ide.execute()


ide = Intellij()
lap1 = Laptop()
lap1.code(ide)