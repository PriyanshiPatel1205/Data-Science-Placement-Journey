#List - stores set of values, it can store elements of different data types, it is mutable (can be changed after creation)
marks = [90, 85, 78.2, 92.4, 88.9]
print(marks)
print(type(marks))  # Output: <class 'list'>

#Accessing list elements using indexing
print(marks[0])
print(marks[2])
print(len(marks))
print(marks[-1])  # accessing the last element of the list using negative indexing

#list is mutable - we can change the elements of the list after creation
student = ["Priya", 21, "Data Science", 3.8, True]
print(student)
#After changing the first element of the list to "Arjun"
student[0] = "Arjun"
print(student)  # Output: ['Arjun', 21, 'Data Science', 3.8, True] 

#slicing a list
marks = [90, 85, 78.2, 92.4, 88.9]
print(marks[1:4]) # slicing from index 1 to 3 (4 is exclusive)
print(marks[:3]) # slicing from the beginning of the list to index 2
print(marks[2:]) # slicing from index 2 to the end of the list
print(marks[-3:-1]) # slicing from index -3 to -2 (exclusive)

#List methods - print(), len(), append(), insert(), remove(), pop(), sort(), reverse()
list = [2, 1, 4]
list.append(5)  # using append() to add an element to the end of the list
print(list)  # Output: [2, 1, 4, 5]
print(list.append(3))  # Output: None (append() does not return anything, it modifies the list in place)
print(list)  # Output: [2, 1, 4, 5, 3]

list.sort()  # using sort() to sort the list in ascending order
print(list)  # Output: [1, 2, 3, 4, 5]
list.sort(reverse=True)  # using sort() with reverse=True to sort the list in descending order
print(list)  # Output: [5, 4, 3, 2, 1]

list1 = ["apple", "cherry", "banana"]
list1.sort()  # sorting a list of strings in alphabetical order
print(list1)  # Output: ['apple', 'banana', 'cherry']
list1.sort(reverse=True)  # sorting a list of strings in reverse alphabetical order
print(list1)  # Output: ['cherry', 'banana', 'apple']

list.reverse()  # using reverse() to reverse the order of the list
print(list)  # Output: [1, 2, 3, 4, 5]

list.insert(2, 10)  # using insert() to add an element at a specific index (inserting 10 at index 2)
print(list)  # Output: [1, 2, 10, 3, 4, 5]

list.remove(10)  # using remove() to remove the first occurrence of a specific element (removing 10 from the list)
print(list)  # Output: [1, 2, 3, 4, 5]

list.pop(3)  # using pop() to remove and return the element at index 3
print(list)  # Output: [1, 2, 3, 4]

#===============================================================================

#Tuples - stores set of values, it can store elements of different data types, it is immutable (cannot be changed after creation)

tup = (1, 2, 3, 4)
print(tup)
print(type(tup))  # Output: <class 'tuple'>
print(tup[0])
print(tup[2])
#tup[0] = 10  # trying to change the first element of the tuple (this will raise an error because tuples are immutable)

tup1 = () # creating an empty tuple
print(tup1)  # Output: ()
print(type(tup1))  # Output: <class 'tuple'>

tup2 = (1,) # creating a tuple with a single element (note the comma after the element)
print(tup2)  # Output: (1,)
print(type(tup2))  # Output: <class 'tuple'> (tup2 is a tuple with a single element)

tup3 = (1) # this is not a tuple, it is just an integer (without the comma, it is not considered a tuple)
print(tup3)  # Output: 1
print(type(tup3))  # Output: <class 'int'> (tup3 is an integer, not a tuple)

#Slicing a tuple
tup = (1, 2, 3, 4, 5)
print(tup[1:4]) # slicing from index 1 to 3 (4 is exclusive)

#Tuple methods - print(), len(), count(), index()
tup = (1, 2, 3, 4, 5, 2)
print(tup.index(3))  # using index() to get the index of the first occurrence of a specific element (getting the index of 3 in the tuple)

print(tup.count(2))  # using count() to get the number of occurrences of a specific element in the tuple (counting how many times 2 appears in the tuple)

#Practice Questions

#Write a program to input names of 3 movies and store them in a list.
name1 = input("Enter name of movie 1: ")
name2 = input("Enter name of movie 2: ")
name3 = input("Enter name of movie 3: ")
movies = [name1, name2, name3]
print("List of movies ", movies)

#WAP to check if a list contains a palindrome of elements.
listpalin = [1, 2, 3, 2, 1] #it is palindrome
listpalin = [1, 2, 3, 2, 1, 2] #it is not palindrome
listcopy = listpalin.copy() #copy() - creates a shallow copy of the list (creates a new list with the same elements as the original list)
listcopy.reverse()
if(listpalin == listcopy):
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")

#WAP to count the number of students with "A" grade in the following tuple.
tuplegrade = ("C", "D", "A", "A", "B", "B", "A", "C", "A")
print("Count of A: ", tuplegrade.count("A")) #using count() to get the number of occurrences of "A" in the tuple

#Store the above tuple in a list and sort them from "A" to "D".
listtup = ["C", "D", "A", "A", "B", "B", "A", "C", "A"] 
listtup.sort()
print("Sorted list: ", listtup)