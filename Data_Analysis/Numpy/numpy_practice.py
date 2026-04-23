import numpy as np
arr = np.array([5, 10, 15, 20, 25])
print(arr.shape)
print(arr.size)
print(arr.ndim)
print(arr.dtype)

arr1 = np.array([[10, 20, 30], [40, 50, 60]])
print(arr1[1,1]) #print element 50
print(arr1[0])  #prints the first row of the array
print(arr1[:,1]) #prints second column

print(arr1 + 10) #add 10 to array
print(arr1 * 2) #multiply by 2
print(arr1 * arr1) #square all elements

print(arr1.sum()) #sum of all elements
print(arr1.mean()) #mean of all elements
print(arr1.min()) #minimum element  
print(arr1.max()) #maximum element