import numpy as np
#print(np.__version__)
myarr = np.array([1,2,3,4,5])
print(myarr)

myarr = np.array([1,2,3,4,5], np.int8) #int8 is a data type that can store integers from -128 to 127 (8-bit signed integer)
print(myarr)
print(myarr.dtype) #prints the data type of the array

# 2-D array
myarr1 = np.array([[1,2,3],[4,5,6]])
print(myarr1)
print(myarr1.dtype) #prints the data type of the array
print(myarr1[0,2]) #prints the element at index 0,2 (3)

myarr2 = np.array([[1,2,3]])
print(myarr2)
print(myarr2.dtype) #prints the data type of the array
print(myarr2[0][1]) #prints the element at index 0,1 (2)
print(myarr2[0,1]) #prints the element at index 0,1 (2)

print(myarr1.shape) #prints the shape of the array (2, 3)
print(myarr2.shape) #prints the shape of the array (1, 3)

myarr2[0][1] = 20 #changes the element at index 0,1 to 20
print(myarr2) #prints the updated array [[ 1 20  3]]

#Creation of numpy arrays

myarr3 = np.array([1,2,3,4,5], dtype=np.float64) #creates a 1-D array of floats
print(myarr3)

#Conversion from python list, tuple, and array to numpy array
mylist = [1,2,3,4,5]
myarr4 = np.array(mylist) #converts a python list to a numpy array
print(myarr4)

mytuple = (1,2,3,4,5)
myarr5 = np.array(mytuple) #converts a python tuple to a numpy array
print(myarr5)

# Intrinsic numpy array creation methods (arange, zeros, ones, linspace, eye)

zerosarr = np.zeros((2,5)) #creates a 2-D array of zeros with shape (2,5)
print(zerosarr)

rngearr = np.arange(15) #creates a 1-D array of integers from 0 to 14
print(rngearr)

rngearr1 = np.arange(1,10,2) #creates a 1-D array of integers from 1 to 9 with a step of 2
print(rngearr1)

lspacearr = np.linspace(0,10,5) #creates a 1-D array of 5 evenly spaced numbers between 0 and 10
print(lspacearr)

lspacearr1 = np.linspace(0,50,5)
print(lspacearr1)

emparr = np.empty((3,4)) #creates a 2-D array of uninitialized values with shape (3,4)
print(emparr)

emp_like = np.empty_like(myarr1) #creates an array of uninitialized values with the same shape and data type as myarr1
print(emp_like)

emp_like1 = np.empty_like(lspacearr1) #creates an array of uninitialized values with the same shape and data type as lspacearr1
print(emp_like1)

ide = np.identity(4) #creates a 2-D array of shape (4,4) with ones on the diagonal and zeros elsewhere
print(ide)
print(ide.shape) #prints the shape of the array (4, 4)

arr = np.arange(99) #creates a 1-D array of integers from 0 to 98
print(arr)
reshapedarr = arr.reshape(11,9) #reshapes the array to a 2-D array with shape (11,9)
print(reshapedarr)

arrorig = reshapedarr.ravel() #flattens the array to a 1-D array
print(arrorig)

#axis 
# for 1 D array, axis 0 is the only axis and it represents the rows [axis 0]
# for 2 D array, axis 0 represents the rows and axis 1 represents the columns [axis 0, axis 1]

x = np.array([[1,4,2],[4,7,6],[0,8,9]]) # 2-D array with shape (3,3)
print(x)
print(x.sum(axis=0)) #sums the elements along the columns (axis 0) and returns a 1-D array [5 19 17]
print(x.sum(axis=1)) #sums the elements along the rows (axis 1) and returns a 1-D array [7 17 17]

print(x.T) #transposes the array (swaps the rows and columns)

print(x.flat) #returns an iterator that iterates over the elements of the array in a flat manner (1-D)
for i in x.flat:
    print(i) #prints each element of the array in a flat manner (1, 4, 2, 4, 7, 6, 0, 8, 9)

print(x.ndim) #prints the number of dimensions of the array (2)
print(x.size) #prints the total number of elements in the array (9)

print(x.nbytes) #prints the total number of bytes consumed by the array (72)

one = np.array([1, 34, 2, 67])
print(one.argmax()) #returns the index of the maximum element in the array (1)

print(one.argmin()) #returns the index of the minimum element in the array (2)
print(one.argsort()) #returns the indices that would sort the array (array([0, 2, 1, 3]))

#for 2D array
print(x.argmax()) #returns the index of the maximum element in the array (8)
print(x.argmin()) #returns the index of the minimum element in the array (6)

print(x.argmax(axis=0)) #returns the indices of the maximum elements along the columns (array([1, 2, 2]))
print(x.argmax(axis=1)) #returns the indices of the maximum elements along the rows (array([1, 1, 2]))

print(x.argsort(axis=0)) #returns the indices that would sort the array along the columns (array([[2, 0, 0], [0, 1, 1], [1, 2, 2]]))

print(x.argsort(axis=1)) #returns the indices that would sort the array along the rows (array([[0, 2, 1], [0, 2, 1], [0, 1, 2]]))

print(x.ravel()) #flattens the array to a 1-D array (array([1, 4, 2, 4, 7, 6, 0, 8, 9]))

print(x.reshape(9,1)) #reshapes the array to a 2-D array with shape (9,1)

y = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(x+y) #adds the two arrays element-wise (array([[ 2,  6,  5], [ 8, 12, 12], [ 7, 16, 18]]))

# [1, 2] + [3, 4] =[1, 2, 3, 4] (concatenation) addition in list is not element-wise but in numpy it is element-wise

print(x*y) #multiplies the two arrays element-wise (array([[ 1,  8,  6], [16, 35, 36], [ 0, 64, 81]]))

print(np.sqrt(x)) #returns the square root of each element in the array (array([[1.        , 2.        , 1.41421356], [2.        , 2.64575131, 2.44948974], [0.        , 2.82842712, 3.        ]]))

print(x.sum()) #returns the sum of all elements in the array (41)
print(x.min()) #returns the minimum element in the array (0)
print(x.max()) #returns the maximum element in the array (9)

print(np.where(x>8)) #returns the indices of the elements that satisfy the condition (array([2]), array([2]))

print(np.count_nonzero(x)) #returns the number of non-zero elements in the array (8)




