import numpy as np
import pandas as pd

# Marks of 5 students
marks = np.array([
    [85, 80, 90],
    [70, 75, 65],
    [92, 88, 95],
    [60, 72, 68],
    [78, 82, 80]
])

print("Marks:")
print(marks)


total = np.sum(marks, axis=1)
print("\nTotal marks:")
print(total)


average = np.mean(marks, axis=1)
print("\nAverage marks:")
print(average)


subject_average = np.mean(marks, axis=0)
print("\nAverage marks in each subject:")
print(subject_average)


highest = np.max(marks, axis=0)
print("\nHighest score in each subject:")
print(highest)


lowest = np.min(marks, axis=0)
print("\nLowest score in each subject:")
print(lowest)


students = np.where(average > 80)
print("\nStudents with average above 80:")
print(students)


status = np.where(average >= 40, "Pass", "Fail")
print("\nPass/Fail status:")
print(status)


highest_student = np.argmax(average)
print("\nIndex of highest-performing student:")
print(highest_student)

standard_deviation = np.std(marks, axis=0)
print("\nStandard deviation of each subject:")
print(standard_deviation)


df = pd.DataFrame({
    "Python": marks[:, 0],
    "SQL": marks[:, 1],
    "Machine Learning": marks[:, 2],
    "Total": total,
    "Average": average,
    "Status": status
})

print("\nFinal DataFrame:")
print(df)