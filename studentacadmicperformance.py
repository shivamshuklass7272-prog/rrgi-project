import numpy as np
import os
os.environ.pop("MPLBACKEND", None)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

dataset = [
    [75, 80, 85],
    [80, 75, 90],
    [90, 85, 80]
]

subjects = ["Physics", "Chemistry", "Biology"]
students = ["Student 1", "Student 2", "Student 3"]

# #1. Total marks of each student.(draw a bar graph for this)
total_marks = np.sum(dataset, axis=1)

print(total_marks)
plt.subplot(2,2,1)
plt.bar(students, total_marks,color=['red', 'yellow', 'green'])






#2. Average marks of each subject and compare it from the marks of each student. (draw a line graph for this)


average_marks = np.mean(dataset, axis=0)

print(average_marks)
plt.subplot(2,2,2)
plt.plot(students, average_marks)



plt.grid()

#3.find the maximum marks in each subject.
# 3. Find maximum marks in each subject

max_marks = np.max(dataset, axis=0)
plt.subplot(2,2,3)
print(max_marks)

plt.plot(subjects, max_marks)



#4. find the minimum marks in each subject.
#display by bar graph
# 4. Find minimum marks in each subject

min_marks = np.min(dataset, axis=0)

print(min_marks)

plt.plot(subjects, min_marks)


plt.show()