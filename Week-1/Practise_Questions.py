#LIST

# Find the largest element in a list
list4 = [1,3, 5, 2, 6, 4]
list4.sort()
print("Largest element:", list4[-1])

# Reverse a list
list1 = [1, 2, 3, 4, 5]
list1.reverse()
print("Reverse: ",list1)

# Remove duplicates from a list
list2 = [1, 2, 3, 2, 2, 3, 1, 4]
list3 = list(set(list2))
print("After removing duplicates: ", list3)

# Count frequency of elements in a list
list5 = [1, 2, 3, 2, 1, 4, 3]
for i in set(list5):
    print("Count of", i, ":", list5.count(i))

# Sort list without using sort()
# Bubble sort algorithm
n = len(list4)
for i in range(n):
    for j in range(0, n-i-1):
        if list4[j] > list4[j+1]:
            list4[j], list4[j+1] = list4[j+1], list4[j]
print("Sorted list: ", list4)

#Tuples

# Convert tuple to list
tup = (1, 2, 3, 4, 5)
print(list(tup))

# Access elements of a tuple
tup1 = (10, 20, 30, 40, 50)
print("First element:", tup1[0])
print("Last element:", tup1[-1])

# Count occurrence of an element in a tuple
tup2 = (1, 2, 3, 1, 3, 1, 2, 1, 3, 3)
for i in set(tup2):
    print("Count of", i, ":", tup2.count(i))

# Tuple unpacking - Taking values from a tuple (or sequence) and assigning them to multiple variables in one line.
tup3 = (10, 20, 30)
a, b, c = tup3
print("a:", a)
print("b:", b)
print("c:", c)

#Set

# Union, Intersection, Difference of sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union: ", set1.union(set2))
print("Intersection: ", set1.intersection(set2))
print("Difference (set1 - set2): ", set1.difference(set2))

# Remove duplicates from a list using set
list6 = [1, 2, 3, 4, 5, 5, 6]
set3 = set(list6)
print("Unique elements: ", set3)

#Dictionary

# Student marks dictionary
student = {"name" : "Priyanshi",
           "marks" : {
                "Maths" : 90,
                "Science" : 95,
                "English" : 85
           }
}
print(student)

# Merge two dictionaries
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
dict1.update(dict2)  # using update() to merge dict2 into dict1 (if there are duplicate keys, the values from dict2 will overwrite the values in dict1)
print("Merged dictionary: ", dict1)

#count word freequency
text = "hello world hello"
word_freq = {}
for word in text.split():
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print("Word frequency: ", word_freq)

#find max value key in a dictionary
scores = {"Alice": 85, "Bob": 92, "Charlie": 88}
max_score = max(scores.values())  # using max() to find the maximum score
for student, score in scores.items():
    if score == max_score:
        print("Student with highest score: ", student)

#nested dictionary access
student1= {"name" : "Priyanshi",
           "marks" : {
                "Maths" : 90,
                "Science" : 95,
                "English" : 85
           }
}
print(student1["marks"]["Science"])  # accessing the marks of Science for the student

#Even & Odd numbers in a list
num = [2, 3, 6, 4, 1, 5]
result = {
    "even": [],
    "odd": []
}
for i in num:
    if i % 2 == 0:
        result["even"].append(i)
    else:
        result["odd"].append(i)
print(result)

#Sort dictionary by values
scores = {"Alice": 85, "Bob": 92, "Charlie": 88}
tuples = (scores.items())  # using items() to get a list of key-value pairs as tuples
sorted_tuples = sorted(tuples, key=lambda x: x[1])  # sorting the list of tuples based on the second element (value) using a lambda function as the key
print("Sorted dictionary by values: ", sorted_tuples)

#Student Attendance Dictionary
present = ["Priya","Raj","Amit","Raj","Priya"]
attendance = {}
for student in present:
    if student in attendance:
        attendance[student] += 1
    else:
        attendance[student] = 1
print("Attendance: ", attendance)