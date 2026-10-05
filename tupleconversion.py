<<<<<<< HEAD
# Take a list of numbers, convert it into a tuple, perform an appropriate tuple operation, then convert it back into a list and modify the resulting list.
numbers = [10, 20, 30, 40, 50]
numbers_tuple = tuple(numbers)
print("Tuple:", numbers_tuple)
print("Number of elements:", len(numbers_tuple))
numbers_list = list(numbers_tuple)
numbers_list.append(60)
print("Final list:", numbers_list)
=======
# # ake a student's marks as input and print their grade according to these conditions:
# 80–100 → A+
# 70–79 → A
# 60–69 → B
# 50–59 → C
# 40–49 → D
# Below 40 → F

marks =int( input("Enter the marks:"))
if (marks >= 80 and marks <=100):
    print("Grade:", "A+")
elif(marks >= 70 and marks <=79):
    print("Grade:", "A")
elif(marks >= 60 and marks <=69):
    print("Grade:", "B")
elif(marks >= 50 and marks <=59):
    print("Grade:", "C")
elif(marks >= 40 and marks <=49):
        print("Grade:", "D")
else:
     print("Grade:", "F")


>>>>>>> adde9bd95c22f6025a6033a47c5cd57d839c255c
