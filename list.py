Marks = [78,98.67,87,70]
print(Marks)
print(type(Marks))
print(len(Marks))
print(Marks[1])

student=["Maria",9,"Dhaka","CSE"]
print(student)
print(student[1])
student[1] = "A"
print(student)

#list slicing
Marks = [78,98.67,87,70]
print(Marks[0:])
print(Marks[:3])
print(Marks[1:3])
print(Marks[-3:-1])


#list methods
list = [8,60,89,54,36]
list.append(34)
print(list)
list.sort()
print(list)
list.sort(reverse = True)
print(list)
list.reverse()
print(list)
list.insert(1,66)
print(list)
list.remove(60)
print(list)
list.pop(2)
print(list)

#tuple
tup = ()
print(tup)
print(type(tup))

tup = (8,60,89,54,36)
print(tup[0])
print(tup[1])
print(tup[1:3])

#tuple methods
tup = (8,60,89,54,36,60,66,60)
print(tup.index(89))
print(tup.count(60))
