#Loops - used to repeat intructions

#while loop 

i=1
while (i<=5):
    print("Hello World")
    i+=1

#print numbers 1 to 5
i=1
while(i<=5):
    print(i)
    i+=1

#print numbers 5 to 1
i=5
while (i>=1):
    print(i)
    i-=1

#Print multiplication table of a number n
n=int(input("Enter a number: "))
i=1
while (i<=10):
    print(n, "*", i, "=", i*n)
    i+=1

#Print the elements of the following list using loops: [1,4,9,16,25,36,49,64,81,100]
i=1
while(i<=10):
    print(i*i)
    i+=1

#Search for a number x in this tuple using loop:
tup=[1,4,9,16,25,36,49,64,81,100]
x=int(input("Enter a number: "))
i=0
while(i<len(tup)):
    if(tup[i]==x):
        print("Element found at index ", i)
    i+=1

#Break and Continue
#Break = used to terminate the loop when encountered
#Continue = terminates the execution in the current iteration & continues execution of loop with next iteration

i=1
while(i<=5):
    print(i)
    if(i==3):
        break
    i+=1

i=1
while(i<=5):
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1

#for loop = used for sequential traversal.
# Traversing list, string, tuples etc.

list = [1,2,3,4,5]
for i in list:
    print(i)

str = "Hello"
for i in str:
    print(i)

# Print the elements of the following list using loop: [1,4,9,16,25,36,49,64,81,100]
list1 = [1,4,9,16,25,36,49,64,81,100]
for i in list:
    print(i)

#Search for number x in this tuple using loop: [1,4,9,16,25,36,49,64,81,100]
tuple = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter a number : "))
for i in tuple:
    if(tuple[i]==x):
        print("Element found at index", i)
        break
    i+=1

#range() - starting from 0 by default
print(range(5))

#range(start, stop, step) - start and step in optional
for i in range(2,10): #range(start, stop)
    print(i)

for i in range(1,10,2): #range(start, stop, step)
    print(i)

#print multiplication table of a number n
n=int(input("Enter a number: "))
for i in range(1,11):
    print(n, "*", i, "=", n*i)

#pass statement - null statement that does nothing.
#It is used as placeholder for future code

for i in range(5):
    pass
print("Hello")

#Practise Questions

# WAP to find sum of first n numbers using while loop

n=int(input("Enter a number: "))
sum=0
i=1
while (i<=n):
    sum=sum+i
    i+=1
print("Sum of first ",n, "numbers: ", sum)

#WAP to find factorial of first n numbers using for loop
n=int(input("Enter a number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of ",n, ": ", fact)