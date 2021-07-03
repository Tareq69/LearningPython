

f = open('Bhrom.txt','r') # Opening a file in reading mode

print(f.read()) # Reading the entire file
for i in range(5):
    print(f.readline(),end="") # Reading the first 5 line of the file


f1 = open('abc.txt','w') # opening a file in writting mode. If the file doesn't exist python
# # will create a file of this name.
f1.write("Hello") # writting something in the file. Remember everytime we write something
# it will overwrite the previous elements in file.

f2 = open('abc.txt','a') # Opening a file in append mode
f2.write(" I am learning python") # appending new elements in the file




