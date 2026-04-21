#print("Hello World!")  # print is a function
#print("Hello", "World!")  # print can take multiple arguments
#print(23)
#print(34+23)  # print can also print the result of an expression

#Variables
# name = "Priyanshi"  # string variable
# age = 22  # integer variable    
# height = 1.75  # float variable
# old = False  # boolean variable
# a = None  # NoneType variable

# print(name)
# print(age)
# print(height)   
# print(old)
# print(a)

#print("My name is", name, "and I am", age, "years old.")  # using variables in print statement

# print(type(name))  # checking the type of variable
# print(type(age))    
# print(type(height))  
# print(type(old))  
# print(type(a))

# x = 2
# y = 3
# sum = x + y  # using variables in an expression
# print(sum)

# Operators
# Arithmetic operators: +, -, *, /, //, %, **
# a = 5
# b = 2
# print(a + b)  # addition
# print(a - b)  # subtraction
# print(a * b)  # multiplication
# print(a / b)  # division
# print(a // b)  # floor division
# print(a % b)  # modulus (remainder)
# print(a ** b)  # exponentiation a^b

# Relational/Comparison operators: ==, !=, >, <, >=, <= (it will return boolean value)
# a = 50
# b = 20
# print(a == b)  # equal to
# print(a != b)  # not equal to   
# print(a > b)  # greater than
# print(a < b)  # less than
# print(a >= b)  # greater than or equal to
# print(a <= b)  # less than or equal to

# Logical operators: and, or, not
# print(True and False)  # logical AND
# print(True or False)  # logical OR  
# print(not True)  # logical NOT
# print(not False)  # logical NOT
# print(not (3>2))  # logical NOT of a comparison
# print("OR: ", (3>2) or (2>3))  # logical OR of two comparisons

# Assignment operators: =, +=, -=, *=, /=, //=, %=, **=
# num = 10
# num = num + 5  # using = operator to assign a new value to num
# print("num: ",num)  # Output: 15
# num+= 5  # using += operator to add 5 to num and assign the result back to num
# print("num: ",num)  # Output: 20
# num-= 3  # using -= operator to subtract 3 from num and assign the result back to num
# print("num: ",num)  # Output: 17
# num*= 2  # using *= operator to multiply num by 2 and assign the result back to num
# print("num: ",num)  # Output: 34
# num/= 4  # using /= operator to divide num by 4 and assign the result back to num
# print("num: ",num)  # Output: 8.5
# num//= 3  # using //= operator to perform floor division of num by 3
# print("num: ",num)  # Output: 2.0
# num%= 3  # using %= operator to get the remainder of num divided by 3
# print("num: ",num)  # Output: 2.0
# num**= 3  # using **= operator to raise num to the power of 3
# print("num: ",num)  # Output: 0.0

#Type conversion
# a = 2
# b = 4.25
# sum = a + b  # adding an integer and a float results in a float because float is superior to int in the type hierarchy
# print("Sum: ", sum)  # Output: 6.25  //automatically converted to float

#Type casting 
# a = "2"  # string variable
# b = 4.25
# sum = int(a) + b  # using int() to convert string to integer before adding
# print("Sum: ", sum)  # Output: 6.25  //a is converted to int before addition

#Input
# name = input("Enter your name: ")  # using input() to get user input (it will always return a string)
# print("Hello, ", name)  # using the input value in a print statement

# val = int(input("Enter a value: "))
# print(type(val), val)  # using int() to convert the input string to an integer before printing its type and value

#DAY - 1 PRACTICE QUESTIONS
# Write a program to input 2 numbers & print their sum.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum: ", num1+num2)

# Write a program to input side of a square & print its area.
side = float(input("Enter the side of the square: "))
print("Area of the square: ", side*side)

# Write a program to input 2 floating point number & print their average.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Average: ", (num1+num2)/2)

# WAP to input 2 int numbers, a and b. 
# Print True if a is greater than or equal tob, else print False.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a >= b)
