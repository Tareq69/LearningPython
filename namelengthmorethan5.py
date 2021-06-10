
lst =[]
x = int(input("Enter the number of names you want in the list: "))

i = 0
while i<x:
    y = input("Enter name in the list: ")
    lst.append(y)
    i +=1

def count(lst):
    for i in lst:
        if len(i) > 5:
            print(i)
        else:
            pass


count(lst)
