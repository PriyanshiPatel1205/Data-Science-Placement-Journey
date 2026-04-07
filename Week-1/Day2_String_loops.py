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



