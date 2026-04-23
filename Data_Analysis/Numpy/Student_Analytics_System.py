import numpy as np
arr1 = np.random.randint(0, 101, 50)
print(arr1) #prints the array of 50 random marks between 0 and 100

average = np.mean(arr1) #calculates the average marks   
print("Average marks: ", average) #prints the average marks

print("Maximum score achieved: ", np.max(arr1)) #prints the maximum score achieved
print("Minimum score achieved: ", np.min(arr1)) #prints the minimum score achieved

count=0
for mark in arr1:
    if mark > 40:
        count+=1
print("Number of students who passed: ", count) #prints the number of students who passed
print("Number of students who failed: ", len(arr1)-count) #prints the number of students who failed

print("Top performers (Top 5 marks): ", np.sort(arr1)[-5:]) #prints the top 5 marks achieved by students

print("Normalized marks: ", arr1/100) #prints the normalized marks (marks divided by 100)


