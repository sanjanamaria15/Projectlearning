student = {
    "name" : "Sanjana Sikder Maria",
    "subjects" : {
        "software eng" : 34,
        "CN" : 34,
        "TOC" :29,
        "Embedded" : 26,
    },
    "roll" : 9,
    "section" : "A"
}
print(student.keys())
print(list(student.keys()))
print(len(student))
print(len(list(student.keys())))
print(student.values())
print(list(student.values()))
print(list(student.items()))
pairs = (list(student.items()))
print(pairs[0])
print(student.get("name"))
student.update({"city" : "Dhaka"})
print(student)


