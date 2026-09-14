# # #Given Array
# # #int a[]={12,16,19,21,26,27,29}
# # #binary Search:
# # #find the index of target element:
# # #int target=27
# # a = [12, 16, 19, 21, 26, 27, 29]

# # target = 27

# # low = 0
# # high = len(a) - 1

# # while low <= high:
# #     mid = (low + high) // 2

# #     if a[mid] == target:
# #         print("Index =", mid)
# #         break
# #     elif a[mid] < target:
# #         low = mid + 1
# #     else:
# #         high = mid - 1


# #Q.2 int arr[]={1,2,5,7,11,13}
# #find the 2 element whose sum is 9
# arr = [1, 2, 5, 7, 11, 13]

# target = 9

# for i in range(len(arr)): 
#     for j in range(i + 1, len(arr)):
#         if arr[i] + arr[j] == target:
#             print(arr[i], arr[j])


# Q3.a1=numpy.arr([5,6],[1,2])
# a2=numpy.arr([2,4],[3,7])
# find the multipacation

import numpy as np
import os
os.environ.pop("MPLBACKEND", None)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

import numpy as np

a1 = np.array([[5, 6], [1, 2]])
a2 = np.array([[2, 4], [3, 7]])

# Matrix multiplication
result = np.dot(a1, a2)

print(result)

# a3=numpy.arrY([[1,2],[3,4][[5,6],[7,8]])
#               FIND THE INDEXES OF 6
import numpy as np

import numpy as np

a3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

print(np.where(a3 == 6))