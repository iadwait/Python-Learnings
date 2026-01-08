print(">>>>> List - Ordered, changeable collection, Allows duplicates")

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits[1])

print(">>>>> Tuple - Ordered, unchangeable (immutable), Allows duplicates")

coordinates = (10,20)
print(coordinates[0])

print(">>>>> Set - Unordered, unique elements only")
numbers = {1,2,3,3,4}
print(numbers) # 3 was removed, 1,2,3,4
numbers.add(5) # 1,2,3,4,5
print(numbers)

print("Dictionary (dict) - Key-value pairs, Unordered, changeable")
person = {"name": "Adwait", "age": 25}
print(person["name"])
person["age"] = 27
person["city"] = "Mumbai"
print(person)