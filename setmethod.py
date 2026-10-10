collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.remove(3)
collection.add((4,5,6))
collection.add("maria")
print(collection)
print(len(collection))
collection.clear()
print(len(collection))

collection2={11,11,55,66,78,78, "hello", "world"}
collection2.pop()
collection2.pop()
print(collection2)

set1 ={1,2,3}
set2 ={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))
