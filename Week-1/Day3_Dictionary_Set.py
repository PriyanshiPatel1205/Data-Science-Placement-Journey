#Dictionary - used to store data values in key:value pairs
#they are unordered, mutable and dont allow duplicate keys

info = {
    "name" : "Priyanshi",
    "age" : 23,
    "subjects" : ["Data Science", "Machine Learning", "Deep Learning"],
    "topics" : ("Python", "R", "SQL"),
    "city" : "Nadiad",
}
print(info)
print(type(info))  # Output: <class 'dict'>

info["name"]  # accessing value using key
print(info["name"])  # Output: Priyanshi
print(info["subjects"])  # Output: ['Data Science', 'Machine Learning', 'Deep Learning']    
print(info["topics"])  # Output: ('Python', 'R', 'SQL')
print(info["city"])  # Output: Nadiad

info["name"] = "Priyanshi Patel"  # updating value of an existing key
print(info["name"])  # Output: Priyanshi Patel

info["country"] = "India"  # adding a new key-value pair to the dictionary
print(info)  # Output: {'name': 'Priyanshi Patel', 'age': 23, 'subjects': ['Data Science', 'Machine Learning', 'Deep Learning'], 'topics': ('Python', 'R', 'SQL'), 'city': 'Nadiad', 'country': 'India'}

null_dict = {}  # creating an empty dictionary
print(null_dict)  # Output: {}

#nested dictionary
student = {
    "name": "Priyanshi",
    "age": 23,
    "subjects": ["Data Science", "Machine Learning", "Deep Learning"],
    "address": {
        "city": "Nadiad",
        "state": "Gujarat",
        "country": "India"
    }
}
print(student["address"]["state"])

#Dictionary methods - keys(), values(), items(), get(), pop(), popitem(), clear()
print(info.keys())  # using keys() to get a list of all keys in the dictionary
print(student.keys())
print(list(info.keys()))  # converting the keys to a list

print(info.values())  # using values() to get a list of all values in the dictionary
print(student.values())
print(list(info.values()))  # converting the values to a list

print(info.items())  # using items() to get a list of all key-value pairs in the dictionary as tuples
print(student.items())
pairs = list(info.items())  # converting the items to a list
print(pairs[0])  # accessing the first key-value pair (as a tuple)

print(student.get("name2"))  # using get() to access the value of a key (returns None if key is not found)
#print(student["name2"])  # accessing the value of a key using square brackets (raises KeyError if key is not found)}])

student.update({"language": "English"})  # using update() to add a new key-value pair to the dictionary
print(student)  

#================================================================================

#Set - collection of unordered items, it is immutable and does not allow duplicate values (only unique values are stored in a set)
#Set is mutable but the elements of a set are immutable (we cannot change the elements of a set after creation, but we can add or remove elements from the set)

nums = {1, 2, 3, 4}
set2 = {1, 2, 2, 3, 4, 4}  # duplicate values will be ignored in a set
print(nums)  # Output: {1, 2, 3, 4}
print(set2)  # Output: {1, 2, 3, 4} (duplicate values are ignored)
print(type(nums))  # Output: <class 'set'>

#we cannot store list and dictionary in a set because they are mutable, but we can store tuples in a set because they are immutable

collection = {1, "Hello", (1, 2, 3)}  # a set can store elements of different data types
print(collection)  # Output: {1, 'Hello', (1, 2, 3)}
print(len(collection))  # using len() to get the number of elements in the set

null_set = set()  # creating an empty set, don't use {} to create an empty set because it will create an empty dictionary instead
print(null_set)  # Output: set()

#Set methods - add(), remove(), discard(), pop(), clear()

nums.add(5)  # using add() to add an element to the set
print(nums)  # Output: {1, 2, 3, 4, 5}

nums.remove(3)  # using remove() to remove a specific element from the set (raises KeyError if element is not found)
print(nums)  # Output: {1, 2, 4, 5}

nums.add("Hello")
print(nums)  # Output: {1, 2, 4, 5, 'Hello'}

#nums.add([1, 2, 3])  # trying to add a list to the set (this will raise an error because lists are mutable and cannot be added to a set)
#print(nums)  # Output: {1, 2, 4, 5, 'Hello'} (the list is not added to the set)

nums.clear()  # using clear() to remove all elements from the set
print(nums)  # Output: set() (the set is now empty)

print(collection.pop())  # using pop() to remove and return an arbitrary element from the set (since sets are unordered, we cannot specify which element to pop)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # using union() to get the union of two sets (all unique elements from both sets)
print(set1.intersection(set2))  # using intersection() to get the intersection of two sets (only the elements that are present in both sets)
print(set1.difference(set2))  # using difference() to get the difference of two sets (only the elements that are present in set1 but not in set2)

#Practice questions

#Store the following word meanings in a python dictionary:
#table - a piece of furniture, list of facts & figures
#cat - a small animal
dict1 = {
    "table" : ("a piece of furniture", "list of facts & figures"), #stored using tuple
    "cat" : "a small animal"
    }
print(dict1)

#You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
subjects = {"python", "java", "C++", "python", "java", "javascript", "C++", "C"}  
print("Total classrooms: ", len(subjects))  # Output: {'python', 'java', 'C++', 'javascript', 'C'} (duplicate values are ignored)

#WAP to enter marks of 3 subjects from the user and store them in a dicitionary.
#Start with an empty dictionary & add one by one.
#Use subject name as key and marks as value in the dictionary.
dict2 = {}
x = int(input("Enter phy: "))
dict2.update({"Phy": x})
x = int(input("Enter a chem: "))
dict2.update({"Chem": x})
x = int(input("Enter a math: "))
dict2.update({"Math": x})
print(dict2)

#Figure out a way to store 9 and 9.0 as separate values in the set.
#(You can take help of built-in data types)
set1 = {9, "9.0"}
print(set1)  

set1={("int", 9), ("float", 9.0)}
print(set1)