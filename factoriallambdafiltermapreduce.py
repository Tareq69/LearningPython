

# def fact(n):
#     if(n==0):
#         return 1
#     return n * fact(n-1)
#
#
# result = fact(10)
# print(result)

# def fact(n):
#     y = 1
#
#     for i in range(1,n+1):
#         y = y*i
#     return y
#
# result = fact(6)
# print("Factorial is: ", result)

from functools import reduce

nums = [2,3,4,5,6,7,8,9,10]

evens = list(filter(lambda n:n%2==0,nums))

inc2 = list(map(lambda n:n+2,evens))

sum = reduce(lambda a,b: a+b,inc2)

print(evens)
print(inc2)
print(sum)

