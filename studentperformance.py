from turtle import st

import numpy as np
import pandas as pd
# marks=np.array([[85, 80,90],
#                 [70,75,65],
#                 [92,88,95],
#                 [60,72,68],
#                 [78,82,80]
#              ])

#1.total mark of each student
# total=np.sum(marks,axis=1)
# print(total)
# #2.averagee of each student
# average=np.mean(marks,axis=1)
# print(average)

# #3. avg of each subject
# average_subject=np.mean(marks,axis=0)
# print(average_subject)

# #4. highest scorein each subject
# highest=np.mean(marks,axis=1)
# print(highest)
# #5. lowest scorte in each subject
# lowest=np.mean(marks,axis=0)
# print(lowest)
# #6. avg markes in avabe in 80
# student=np.where(average>80)
# print(student)

# #7. np.where() to assing pass or fail status
# status=np.where(average>=40,"pass","fail")
# print(status)
# #8. find the index of highest performing student 
# index=np.argmax(average)
# print(index)

# #8.
# std=np.std(marks,axis=0)
# print(std)

# #10.
# import pandas as pd
# df=pd.DataFrame(
#     marks,columns=["python","sql","machain leraning"]
# )
# print(df)

#Q no 2
import numpy as np
salary=np.array([
    [25000,2,80],
    [45000,5,90],
    [30000,3,75],
    [60000,8,95],
    [35000,4,85]
])
#1.calculate the avg salary
avg_salary=np.mean(salary[:,0])
print(avg_salary)
#2.
max_salary=np.max(salary[:,0])
print(max_salary)
#3.
min_salary=np.min(salary[:,0])
print(min_salary)
#4.
avg_salary=np.mean(salary[:,0])
print(avg_salary)
#5.
avg_salary=np.where(salary[:,0]>40000)
print(avg_salary)
#6th
avg_salary=np.mean(salary[:,2]>80)
print(avg_salary)
#7yh
index=np.argmax(salary[:,2])
print(index)
#8th
std=np.mean(salary[:,2])
print(std)
#9
status = np.where(salary[:, 0] > 40000, "high salary", "low salary")

print(status)
shudent=np.save("student_performance.npy", salary)
print(shudent)