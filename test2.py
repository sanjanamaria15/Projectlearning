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



