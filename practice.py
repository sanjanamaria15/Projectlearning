#WAP to input users first name and print it's length
Name = input("Enter users name:")
print("Length of users name is:" ,len(Name))

#WAP to find the occurence of $ in a string.
str = "Hi, $I am the $ symbol $99.99."
print(str.count("$"))

#odd or even
num = int(input("enter number:"))
if(num % 2 == 0):
    print("EVEN")
else:
    print("ODD")

#greatest number
a = int(input("enter first number:")) 
b = int(input("enter second number:")) 
c = int(input("enter third number:")) 
if(a >= b and a >= c):
    print("the greatest is:", a)
elif(b >= c):
    print("the greatest is:", b)
else:
    print("the greatest is:", c)

#multiple of 7
num = int(input("enter number:"))
if(num % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple")
