# Take a list of numbers, convert it into a tuple, perform an appropriate tuple operation, then convert it back into a list and modify the resulting list.
numbers = [10, 20, 30, 40, 50]
numbers_tuple = tuple(numbers)
print("Tuple:", numbers_tuple)
print("Number of elements:", len(numbers_tuple))
numbers_list = list(numbers_tuple)
numbers_list.append(60)
print("Final list:", numbers_list)