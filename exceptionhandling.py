

a = 5
b = 0


try:
    print(a / b)
except Exception as e:
    print("You can't divide by 0", e)

finally:
    print("Resource closed")
