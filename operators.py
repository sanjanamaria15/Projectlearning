#arithmetic operators
a = 46
b =22
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)#remainder
print(a ** b) #a^b

#relational operators
a = 46
b = 22
print(a == b) #False
print(a != b) #True
print(a > b) #True
print(a >= b)#True
print(a < b) #False
print(a <= b) #False

#assignment operators
num = 10
num = num+10
print("num :", num)

num  = 20
num -= 10
print("num :", num)

num = 30
num *= 10
print("num :", num)

num = 30
num /= 2
print("num :", num)

num = 30
num %= 10
print("num :", num)

num =23
num **= 4
print("num :", num)


#logical operators
#not operator
print(not False)
print(not True)
print(not(a>b))
print(not(a<b))

#AND operator
a= 50
b=30
print(not(a<b))
val1 = True
val2 =True
print("and operator :", val1 and val2)

val1 = True
val2 = False
print("AND operator :", val1 and val2)
#if any value is False it will return False


#OR operator
val1 = False
val2 = True
print("OR opertator :", val1 or val2)
#if any value is true it will return true
a = 50
b =20
print("OR operator :", (a == b) or (a<b))


#type conversion
#type casting
a = int("2")
b = 4.25
sum = a + b
print(sum)
print(type(a))

