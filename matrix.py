import numpy as np

m2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(m2)
#traversal
#1 2 3 4 5 6 7 8 9
for i in np.nditer(m2):
    print(i,end="")

#transpose a matrix 
print()
mt2 = m2.T
print(mt2)

import numpy as np

matrix1 = np.array([[100, 200], [300, 400]])
matrix2 = np.array([[1, 2], [3, 4]])

# Dot product of matrix
matrix3 = np.dot(matrix1, matrix2)

print(matrix3)
#add 2 in every element of matrix1
print(matrix3+2)

#twice all element of matrix1
print(matrix1*2)

# Create a 3D array and traverse it.
m3 = np.array([[[1,2],[3,4],[5,6]]])
print(m3)
for i in np.nditer(m3):
    print(i, end=" ")

a = 3
b = 5
print("\nBitwise AND of a and b is", np.bitwise_and(a, b))

marks = np.array([
    [80, 70, 90],
    [85, 95, 80],
    [90, 85, 85],
])
print("Average marks:", np.mean(marks, axis=0))
print("Maximum marks:", np.max(marks, axis=0))
#python ,java ,sql
#avrage of marks in python
#maximum marks in sql




