# Create a NumPy 2D array representing:

# Rows → Students
# Columns → Subjects

# Conditions:

# Minimum 5 students
# Minimum 3 subjects
# Marks range between 0–100

import numpy as np
arr = np.array([[85, 35, 78], [92, 88, 95], [75, 80, 82], [40, 91, 89], [80, 85, 87]])
print(arr) #prints the 2D array of student marks

# Basic Dataset Information
# Total number of students
# Total number of subjects
# Shape of dataset

print("Total number of students: ", arr.shape[0]) #prints the number of rows (students)
print("Total number of subjects: ", arr.shape[1]) #prints the number of columns (subjects)
print("Shape of dataset: ", arr.shape) #prints the shape of the array (5, 3)

avg_student = np.mean(arr, axis=1) #calculates the average marks of each student along the rows (axis 1)
print("Average marks of each student: ", avg_student) #prints the average marks of each

avg_subject = np.mean(arr, axis=0) #calculates the average marks of each subject along the columns (axis 0)
print("Average marks of each subject: ", avg_subject) #prints the average marks of each

print("Topper student index: ", np.argmax(avg_student)) #prints the index of the student with the highest average marks (0-based index)

print("Fail student index: ", np.where(arr < 40)) #prints the indices of students who have an average mark less than 40 (0-based index)

print("Highest marks per subject: ", np.max(arr, axis=0)) #prints the highest marks obtained in each subject along the columns (axis 0)
print("Lowest marks per subject: ", np.min(arr, axis=0)) #prints the lowest marks obtained in each subject along the columns (axis 0)

overavg = np.mean(arr) #calculates the overall average marks of all students and subjects
print(np.where(arr > overavg)) #prints the indices of students who have marks above the overall average (0-based index)

addmarks = arr + 10 #adds 10 marks to each student's marks
print("Marks after adding 10: ", addmarks) #prints the new marks after adding 10
print(np.clip(addmarks, 0, 100)) #prints the array with values clipped between 0 and 100

grades = np.empty(arr.shape, dtype=str) #creates an empty array of the same shape as arr to store grades
grades[arr >= 90] = 'A' #assigns grade 'A' to marks greater than or equal to 90
grades[(arr >= 80) & (arr < 90)] = 'B' #assigns grade 'B' to marks between 80 and 89
grades[(arr >= 70) & (arr < 80)] = 'C' #assigns grade 'C' to marks between 70 and 79
grades[(arr >= 60) & (arr < 70)] = 'D' #assigns grade 'D' to marks between 60 and 69
grades[arr < 60] = 'F' #assigns grade 'F' to marks less than 60

print("Grades: ", grades) #prints the array with grades assigned based on marks
