
class A:

    def show(self):
        print("In a Show")

class B(A):
     def show(self):
        print("In B show")

a = B()
a.show()