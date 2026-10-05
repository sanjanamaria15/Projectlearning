<<<<<<< HEAD
# Take a list of numbers and find the second-largest value without using the sort() or max() methods
numbers = [10, 50, 30, 80, 40]

largest = numbers[0]
second_largest = numbers[0]

for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number

print("Second largest:", second_largest)



=======
# Take a number as input and check whether it is positive, negative, or zero.
num = int(input("Enter a number:"))
if(num > 0):
    print("Positive")
elif(num < 0):
    print("Negative")
else:
    print("Zero")
>>>>>>> adde9bd95c22f6025a6033a47c5cd57d839c255c
