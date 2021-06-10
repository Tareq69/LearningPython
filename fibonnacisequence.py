
def fibo(n):
    num1 = 0
    num2 = 1

    if(n<0):
        print("Invalid input")
    elif(n==1):
        print(num1)
    else:
        print(num1)
        print(num2)
        for i in range(2, n):
            x = num1 + num2
            num1 = num2
            num2 = x
            print(x)


z = int(input("Enter the number untill which you want the fibonncai sequence"))
fibo(z)


