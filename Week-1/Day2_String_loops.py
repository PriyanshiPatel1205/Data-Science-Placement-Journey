#Strings
str1 = "Hello World"
str2 = 'Python Programming'
str3 = """This is a multi-line string."""

#escape sequence characters - used for formatting strings
str4 = "This is a string with a newline character.\nThis is the second line."
print(str4)
str5 = "This is a string with a tab character.\tThis is after the tab."
print(str5)

#concatenation
print("Concatenation: ",str1+str2) # concatenating two strings
str6 = str1 + " " + str2  # concatenating with a space in between
print("Concatenation with space: ", str6)

#length of a string
print("Length of str1: ", len(str1))  # using len() function to get the length of a string
print("Length of str6: ", len(str6)) #space is also counted as a character

#Indexing - in python, indexing starts from 0 (only used for accesing the characters, you cannot change the characters of a string using indexing as strings are immutable)
print(str1[3]) # accessing the character at index 3 of str1

#Slicing - used to get a substring from a string
print(str1[0:5]) # slicing from index 0 to 4 (5 is exclusive)
print(str1[6:]) # slicing from index 6 to the end of the string
print(str1[:5]) # slicing from the beginning of the string to index 4
print(str1[:]) # slicing the entire string (creates a copy of the string)

#Special case - negative indexing (used to access characters from the end of the string)
print(str1[-1]) # accessing the last character of str1
print(str1[-5:-1]) # slicing from index -5 to -2 (exclusive) 

#String functions
print("Uppercase: ", str1.upper()) # using upper() to convert the string to uppercase
print("Lowercase: ", str1.lower()) # using lower() to convert the string to lowercase
print("Title Case: ", str1.title()) # using title() to convert the string to title case (first letter of each word is capitalized)
print("Ends with 'World': ", str1.endswith("World")) # using endswith() to check if the string ends with a specific substring
print("Starts with 'Hello': ", str1.startswith("Hello")) # using startswith() to check if the string starts with a specific substring
print("Replace 'World' with 'Python': ", str1.replace("World", "Python")) # using replace() to replace a specific substring with another substring
print("Find 'o': ", str1.find("o")) # using find() to get the index of the first occurrence of a specific substring (returns -1 if not found)
print("Count 'o': ", str1.count("o")) # using count() to get the number of occurrences of a specific substring in the string    

#Write a program to input user's firstname and print its length
#firstname = input("Enter your firstname: ")
#print("Length of your firstname: ", len(firstname))

#WAP to count occurrences of $
dollarstr = "$$hello$$world$$"
print("Count of $: ",dollarstr.count("$"))

#=================================================================#
#CONDITIONAL STATEMENTS

#if-elif-else statements

age = 21
if(age>=18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#WAP to check if a number enterred by user is odd or even
num=int(input("Enter a number: "))
if(num%2==0):
    print("It is an even number.")
else:
    print("It is an odd number.")

#WAP to find the greatest of 3 numbers entered by the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if(num1>=num2 and num1>=num3):
    print("Largest number: ", num1)
elif(num2>=num1 and num2>=num3):
    print("Largest number: ", num2)
else:
    print("Largest number: ", num3)

#WAP to check if a number is a multiple of 7 or not
num4= int(input("Enter a number: "))
if(num4%7==0):
    print("It is multiple of 7.")
else:
    print("It is not a multiple of 7.")