# Take a person's age as input and check whether they are eligible to vote. Assume the minimum voting age is 18.
age = int(input("Age:"))
if(age >= 18):
    print("Can vote")
else:
    print("Cannot vote")