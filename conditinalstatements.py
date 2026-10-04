age = 15
if(age >=18):
   print("can vote")
   print("can drive")
else:
   print("cannot vote")

#
light = "pink"
if(light == "yellow"):
    print("Wait")
elif(light == "red"):
    print("stop")
else:
    print("Light is broken")    
# the tab space is called indentation
#if will print when the statement is true
#elif will print when if is false
#else will print when if and elif statement is false

#nesting
age = 87
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    ("can drive")