from time import sleep
from threading import Thread # Using thread to run two function parallaly using two thread


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1) # Execute Hello then wait 1 sec for Hi to execute

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi") #Execute Hi then wait 1 sec for Hello to execute
            sleep(1)


a1 = Hello()
a2 = Hi()
# Important thing to notice is Main thread will run a1 and a2 thread
a1.start() # Start method creates a new thread a1. We are using start method instead of run cause
# its override the run method
sleep(0.2) # To avoid collision
a2.start() # Start method creates a new thread a1. We are using start method instead of run cause
# its override the run method

a1.join() # Main thread will wait untill a1 joins a2 and then execute Bye
a2.join() # Main thread will wait untill a1 joins a2 and then execute Bye

print("Bye")