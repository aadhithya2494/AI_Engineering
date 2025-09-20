import numpy as np

# create 1D array
arr = np.array([10, 20, 30, 40, 50, 60])
print("Original array:", arr)

print("arr[2:]:", arr[2:])         

print("arr[3:5]:", arr[3:5]) 

print("arr[-4]:", arr[-4]) 

print("Reversed array:", arr[::-1]) 

print("ndim - 1d:", arr.ndim) 
print("shape - 1d:", arr.shape) 

# create 2D array
TwoDArray = np.array([[1, 2, 3, 4],
                        [5, 6, 7, 8]])

print("TwoDArray:\n", TwoDArray)

print("TwoDArray[0][1]:", TwoDArray[0][1]) 
print("TwoDArray[1][1]:", TwoDArray[1][1])  
print("TwoDArray[0][3]:", TwoDArray[0][3])  


total = 0
for i in range(TwoDArray.shape[0]):      
    for j in range(TwoDArray.shape[1]):  
        total += TwoDArray[i][j]

print("Sum of all elements:", total)

print("ndim - 2d:", TwoDArray.ndim) 
print("shape - 2d:", TwoDArray.shape) 

# create 3D array
ThreeDArray = np.array([[[1, 2, 3],
                        [4, 5, 6]],
                       [[7, 8, 9],
                        [10, 11, 12]]])

print("3D array:\n", ThreeDArray)

print("ThreeDArray[0,0,0]:", ThreeDArray[0,0,0])   
print("ThreeDArray[0,1,2]:", ThreeDArray[0,1,2])   
print("ThreeDArray[1,1,2]:", ThreeDArray[1,1,2])   

print("ndim:", ThreeDArray.ndim) 