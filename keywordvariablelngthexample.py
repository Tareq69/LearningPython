
def person(name, **data):
    print(name)

    for i,j in data.items():
        print(i,j)


person('Tamim',age="16",city="Dhaka",Mobile="01636710892")