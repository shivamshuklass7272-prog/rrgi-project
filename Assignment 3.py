import pandas as pd
import numpy as np
import os
os.environ.pop("MPLBACKEND", None)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

data = {
    "Semester": [
        1,1,1,1,1,1,1,1,1,
        2,2,2,2,2,2,2,2,2,2,
        3,3,3,3,3,3,3,3,3,3,
        4,4,4,4,4,4,4,4,4,4,
        5,5,5,5,5,5,5,5,5,5,
        6,6,6,6,6,6,6,6,6
    ],

    "Subject": [
        "Engineering Chemistry",
        "Engineering Mathematics-I",
        "Fundamentals of Electrical Engineering",
        "Programming for Problem Solving",
        "Environment and Ecology",
        "Engineering Chemistry Lab",
        "Basic Electrical Engineering Lab",
        "Programming for Problem Solving Lab",
        "Engineering Graphics & Design Lab",

        "Engineering Physics",
        "Engineering Mathematics-II",
        "Fundamentals of Electronics Engineering",
        "Fundamentals of Mechanical Engineering",
        "Soft Skills",
        "Engineering Physics Lab",
        "Basic Electronics Engineering Lab",
        "English Language Lab",
        "Workshop Practice Lab",
        "Sports and Yoga",

        "Material Science",
        "Technical Communication",
        "Data Structure",
        "Computer Organization and Architecture",
        "Discrete Structures & Theory of Logic",
        "Cyber Security",
        "Data Structure Lab",
        "Computer Organization and Architecture Lab",
        "Web Designing Workshop",
        "Internship Assessment / Mini Project",

        "Mathematics-IV",
        "Universal Human Value and Professional Ethics",
        "Operating System",
        "Theory of Automata and Formal Languages",
        "Object Oriented Programming with Java",
        "Python Programming",
        "Operating System Lab",
        "Object Oriented Programming with Java Lab",
        "Cyber Security Workshop",
        "Sports and Yoga-II",

        "Database Management System",
        "Web Technology",
        "Design and Analysis of Algorithm",
        "Object Oriented System Design with C++",
        "Application of Soft Computing",
        "Database Management System Lab",
        "Web Technology Lab",
        "Design and Analysis of Algorithm Lab",
        "Mini Project or Internship Assessment",
        "Constitution of India",

        "Software Engineering",
        "Data Analytics",
        "Computer Networks",
        "Blockchain Architecture Design",
        "Idea to Business Model",
        "Software Engineering Lab",
        "Data Analytics Lab",
        "Computer Networks Lab",
        "Essence of Indian Traditional Knowledge"
    ],

    "Marks": [
        63,68,68,70,72,97,98,98,98,
        69,68,79,51,72,95,91,96,94,89,
        74,81,75,74,71,66,98,98,98,79,
        78,80,69,62,73,62,98,98,98,99,
        60,77,63,80,75,99,99,99,99,69,
        72,79,80,81,70,98,98,98,76
    ]
}

df = pd.DataFrame(data)

print(df)

print("\nNumber of semesters =", df["Semester"].nunique())

print("Total subjects =", len(df))

print("Highest marks =", np.max(df["Marks"]))

print("Lowest marks =", np.min(df["Marks"]))

total = df.groupby("Semester")["Marks"].sum()

print("\nSemester wise total marks")
print(total)

print("Highest total marks =", np.max(total))
print("Lowest total marks =", np.min(total))

print("\nFirst five records")
print(df.head())

average = df.groupby("Semester")["Marks"].mean()

print("\nSemester wise average marks")
print(average)

subject_average = df.groupby("Subject")["Marks"].mean()

print("\nSubject wise average marks")
print(subject_average)

highest = df["Marks"].max()

print("\nHighest performing subject")

for i in range(len(df)):
    if df["Marks"][i] == highest:
        print(df["Subject"][i], df["Marks"][i])

lowest = df["Marks"].min()

print("\nLowest performing subject")

for i in range(len(df)):
    if df["Marks"][i] == lowest:
        print(df["Subject"][i], df["Marks"][i])

best = average.idxmax()
worst = average.idxmin()

print("\nBest semester =", best)
print("Worst semester =", worst)

sem1 = average[1]
sem6 = average[6]

print("\nSemester 1 average =", sem1)
print("Semester 6 average =", sem6)
print("Improvement =", round(sem6 - sem1, 2))

marks = np.array(df["Marks"])

print("\nMean =", np.mean(marks))
print("Median =", np.median(marks))
print("Maximum =", np.max(marks))
print("Minimum =", np.min(marks))
print("Standard Deviation =", np.std(marks))

class_average = np.array([70,72,74,73,75,76])

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

ax[0,0].plot(average.index, average.values, marker="o")
ax[0,0].set_title("Semester Wise Average")
ax[0,0].set_xlabel("Semester")
ax[0,0].set_ylabel("Average Marks")

ax[0,1].bar(range(len(subject_average)), subject_average.values)
ax[0,1].set_title("Subject Wise Average")
ax[0,1].set_xlabel("Subject")
ax[0,1].set_ylabel("Average Marks")

ax[1,0].bar(total.index, total.values)
ax[1,0].set_title("Semester Wise Total")
ax[1,0].set_xlabel("Semester")
ax[1,0].set_ylabel("Total Marks")

ax[1,1].plot(
    average.index,
    average.values,
    marker="o",
    label="My Performance"
)

ax[1,1].plot(
    average.index,
    class_average,
    marker="o",
    label="Class Average"
)

ax[1,1].axhline(
    75,
    linestyle="--",
    label="Target 75%"
)

ax[1,1].set_title("My Performance vs Class Average")
ax[1,1].set_xlabel("Semester")
ax[1,1].set_ylabel("Average Marks")
ax[1,1].legend()

plt.tight_layout()
plt.show()

print("\nObservations")

print("1. Semester", best, "is my best semester.")

print("2. Semester", worst, "is my worst semester.")

print("3. My highest marks are", np.max(marks))

print("4. My lowest marks are", np.min(marks))

print(
    "5. My performance changed by",
    round(sem6 - sem1, 2),
    "marks from Semester 1 to Semester 6."
)


summary = [
    f"Number of semesters : {df['Semester'].nunique()}",
    f"Total subjects      : {len(df)}",
    f"Highest marks       : {np.max(marks)}",
    f"Lowest marks        : {np.min(marks)}",
    f"Best semester       : Semester {best}",
    f"Worst semester      : Semester {worst}",
    f"Semester 1 average  : {sem1:.2f}",
    f"Semester 6 average  : {sem6:.2f}",
    f"Improvement         : {sem6 - sem1:.2f} marks",
]
box_width = max(len(line) for line in summary) + 4
border = "+" + "-" * box_width + "+"

print("\n" + border)
print("|" + "Student Performance Analysis".center(box_width) + "|")
print(border)
for line in summary:
    print("| " + line.ljust(box_width - 2) + " |")
print(border)