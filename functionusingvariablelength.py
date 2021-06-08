def add(a,*b):
    c = a

    for i in b:
        c = c+i

    print("Addition of the arguments are", c)


add(23,45,67)