import importlib
import sys
from pathlib import Path

# Keep this learning file while allowing other scripts to import real NumPy.
project_dir = Path(__file__).resolve().parent
original_path = sys.path[:]
sys.path = [entry for entry in sys.path if Path(entry or ".").resolve() != project_dir]
sys.modules.pop("numpy", None)
try:
    np = importlib.import_module("numpy")
finally:
    sys.path = original_path
sys.modules["numpy"] = np

# 1D Array
arr = np.array([1, 2, 3, 4, 5])

"""print(arr)
print(arr[1])
print(arr.ndim)

print(arr + 2)
print(arr)

print(arr.ndim)
print(sum(arr))
print(max(arr))
print(min(arr))

print(arr[2])
print(arr[1:4])
print(arr[0:])"""

# 2D Array
"""arr2 = np.array([[1, 2, 3], [4, 5, 6],[7,8,9]])

print(arr2)
print(arr2.ndim)
# traverse the 2d arrays
for i in arr2:
    
    for j in i :
        print(j)
# Sum of all elements in 2D array
sum = 0

for i in arr2:
    for j in i:
        sum = sum + j

print("Sum of all elements =", sum)"""

# 3D Array
arr3 = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])

print(arr3)
print(arr3.ndim)


# Traverse 3D array
for i in arr3:
    for j in i:
        for k in j:
            print(k)

 # Sum of all elements
sum = 0

for i in arr3:
    for j in i:
        for k in j:
            sum = sum + k

print("Sum =", sum)













#creat a 3D array and traverse  it.
#sum of all element
"""def sum (n):
    total = 0
    for i in range (n+1):
        total +=i
    return total
result = sum(2)
print(result)"""