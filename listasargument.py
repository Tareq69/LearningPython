
lst = []
x = int(input("Enter the length of the list: "))
i = 0
while i<x:
    y = int(input("Enter element of the list"))
    lst.append(y)
    i+=1
print(lst)
def count(lst):
    e = 0
    o = 0
    for i in lst:
        if i%2==0:
            e +=1
        else:
            o+=1
    return e,o

even,odd = count(lst)
print("Even : {} and odd : {}".format(even,odd))