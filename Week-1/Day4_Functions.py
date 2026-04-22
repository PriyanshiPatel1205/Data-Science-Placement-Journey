#Functions - block of statement that perform a specific task
#def func(param1, param2, .....)

def sum(a,b): #parameters
    return(a+b)
print(sum(5,10)) #function call; arguments

def print_hello():
    print("hello")
print_hello()
print_hello()

#average of 3 numbers
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))
def avg(a,b,c):
    average=(a+b+c)/3
    return average
result = avg(a,b,c)
print("Average of",a,b,c, ": ", result)

#Built-in functions - print(), len(), type(), range()
#User defined functions

#Practise Questions

#WAP to print the length of a list (pass list as parameter)
nums = [1,2,3,4,5]
def length(list):
    print(len(list))
length(nums)

#WAP to print the element of list in a single line (pass list as parameter)
nums = [1,2,3,4,5]
def length(list):
    for i in list:
        print(i , end=" ")
length(nums)

#WAF to find factorial of n (n is the parameter)
num = int(input("Enter a number: "))
def fact(n):
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    return factorial

result = fact(num)
print("Factorial of ",num, ": ", result)

#WAP to convert USD to INR
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")
converter(1)

#Even Odd 
num = int(input("Enter a number: "))
def even_odd(n):
    if(n%2==0):
        print(n, "is even")
    else:
        print(n, "is odd")

even_odd(num)