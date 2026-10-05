#WAP to ask user to enter names of their 3 favorite movie & store them in a list
movies = []
mov1 = input("Enter first movie:")
mov2 = input("Enter second movie:")
mov3 = input("Enter third movie:")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

#WAP to check if a list contains a palindrome of elements
list1 =[1,2,1]
list =[1,2,3]
copy_list1 = list.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not palinedrome")

#WAP to count the number of students with the "A" grade in the following list
grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))

#Store the above values in a list & sort them from "A" to "D"
grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)




