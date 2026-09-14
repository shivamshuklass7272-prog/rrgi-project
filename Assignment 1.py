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


# ============================================================
# PROJECT 2: EMPLOYEE SALARY ANALYSIS
# ============================================================
salary = np.array([
    [25000, 2, 80],
    [45000, 5, 90],
    [30000, 3, 75],
    [60000, 8, 95],
    [35000, 4, 85]
])

salary_average = np.mean(salary[:, 0])
salary_highest = np.max(salary[:, 0])
salary_lowest = np.min(salary[:, 0])
experience_average = np.mean(salary[:, 1])
high_salary = np.where(salary[:, 0] > 40000)[0]
high_performance = np.where(salary[:, 2] > 80)[0]
best_employee = np.argmax(salary[:, 2])
salary_std = np.std(salary[:, 0])
salary_status = np.where(salary[:, 0] > 40000, "High Salary", "Low Salary")

salary_df = pd.DataFrame(salary, columns=["Salary", "Experience", "Performance"])
salary_df["Status"] = salary_status

print("\nPROJECT 2: EMPLOYEE SALARY ANALYSIS")
print("Average salary:", salary_average)
print("Highest salary:", salary_highest)
print("Lowest salary:", salary_lowest)
print("Average experience:", experience_average)
print("Employees with salary above 40000:", high_salary)
print("Employees with performance above 80:", high_performance)
print("Highest-performance employee index:", best_employee)
print("Salary standard deviation:", salary_std)
print(salary_df)


# ============================================================
# PROJECT 3: SALES PERFORMANCE ANALYSIS
# ============================================================
sales = np.array([
    [12000, 15000, 18000],
    [10000, 14000, 16000],
    [18000, 20000, 22000],
    [9000, 12000, 15000],
    [15000, 17000, 19000]
])

sales_total = np.sum(sales, axis=1)
sales_average = np.mean(sales, axis=1)
sales_highest_month = np.max(sales, axis=0)
sales_lowest_month = np.min(sales, axis=0)
best_salesperson = np.argmax(sales_total)
above_average_sales = np.where(sales_average > 15000)[0]
company_monthly_sales = np.sum(sales, axis=0)
sales_std = np.std(sales, axis=0)
sales_category = np.where(
    sales_average >= 18000,
    "Excellent",
    np.where(sales_average >= 14000, "Good", "Needs Improvement")
)

sales_df = pd.DataFrame(sales, columns=["January", "February", "March"])
sales_df["Total Sales"] = sales_total
sales_df["Average Sales"] = sales_average
sales_df["Category"] = sales_category

print("\nPROJECT 3: SALES PERFORMANCE ANALYSIS")
print("Total sales of each salesperson:", sales_total)
print("Average monthly sales:", sales_average)
print("Highest sales in each month:", sales_highest_month)
print("Lowest sales in each month:", sales_lowest_month)
print("Highest total-sales salesperson index:", best_salesperson)
print("Salespersons above 15000 average:", above_average_sales)
print("Total company sales per month:", company_monthly_sales)
print("Monthly sales standard deviation:", sales_std)
print(sales_df)


# ============================================================
# PROJECT 4: STUDENT ATTENDANCE ANALYSIS
# ============================================================
attendance = np.array([
    [90, 85, 95, 88],
    [75, 80, 70, 78],
    [95, 92, 98, 96],
    [65, 70, 72, 68],
    [85, 88, 90, 87]
])

student_attendance = np.mean(attendance, axis=1)
subject_attendance = np.mean(attendance, axis=0)
highest_attendance = np.max(attendance, axis=0)
lowest_attendance = np.min(attendance, axis=0)
above_80_attendance = np.where(student_attendance > 80)[0]
best_attendance_student = np.argmax(student_attendance)
attendance_std = np.std(attendance, axis=0)
attendance_status = np.where(student_attendance >= 75, "Eligible", "Not Eligible")

attendance_df = pd.DataFrame(
    attendance,
    columns=["Python", "Java", "SQL", "ML"]
)
attendance_df["Average Attendance"] = student_attendance
attendance_df["Status"] = attendance_status

print("\nPROJECT 4: STUDENT ATTENDANCE ANALYSIS")
print("Average attendance of each student:", student_attendance)
print("Average attendance of each subject:", subject_attendance)
print("Highest attendance in each subject:", highest_attendance)
print("Lowest attendance in each subject:", lowest_attendance)
print("Students above 80%:", above_80_attendance)
print("Highest-average student index:", best_attendance_student)
print("Attendance standard deviation:", attendance_std)
print(attendance_df)


# ============================================================
# PROJECT 5: PRODUCT SALES ANALYSIS
# ============================================================
product_sales = np.array([
    [100, 120, 150],
    [80, 100, 130],
    [150, 160, 180],
    [70, 90, 110],
    [120, 140, 160]
])

product_total = np.sum(product_sales, axis=1)
product_average = np.mean(product_sales, axis=1)
best_product = np.argmax(product_total)
worst_product = np.argmin(product_total)
high_product = np.where(product_average > 120)[0]
product_monthly_total = np.sum(product_sales, axis=0)
product_std = np.std(product_sales, axis=0)
product_status = np.where(product_average > 120, "High", "Low")

product_df = pd.DataFrame({
    "Product": ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5"],
    "Total Sales": product_total,
    "Average Sales": product_average,
    "Status": product_status
})

print("\nPROJECT 5: PRODUCT SALES ANALYSIS")
print("Total sales of every product:", product_total)
print("Average monthly sales:", product_average)
print("Best-selling product index:", best_product)
print("Worst-selling product index:", worst_product)
print("Highest sales in each month:", np.max(product_sales, axis=0))
print("Lowest sales in each month:", np.min(product_sales, axis=0))
print("Products with average sales above 120:", high_product)
print("Total sales for each month:", product_monthly_total)
print("Sales standard deviation:", product_std)
print(product_df.sort_values("Total Sales", ascending=False))


# ============================================================
# PROJECT 6: WEATHER DATA ANALYSIS
# ============================================================
temperature = np.array([
    [32, 34, 35, 33, 31],
    [28, 30, 31, 29, 27],
    [35, 36, 38, 37, 34],
    [25, 27, 29, 28, 26]
])
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

city_average_temperature = np.mean(temperature, axis=1)
city_maximum_temperature = np.max(temperature, axis=1)
city_minimum_temperature = np.min(temperature, axis=1)
day_average_temperature = np.mean(temperature, axis=0)
hot_day = days[np.argmax(day_average_temperature)]
cool_day = days[np.argmin(day_average_temperature)]
highest_temperature_city = np.argmax(city_average_temperature)
hot_cities = np.where(city_average_temperature > 30)[0]
temperature_std = np.std(temperature)
temperature_status = np.where(temperature >= 35, "Hot", "Normal")

temperature_df = pd.DataFrame(temperature, columns=days)
temperature_df["Average Temperature"] = city_average_temperature

print("\nPROJECT 6: WEATHER DATA ANALYSIS")
print("Average temperature of each city:", city_average_temperature)
print("Maximum temperature of each city:", city_maximum_temperature)
print("Minimum temperature of each city:", city_minimum_temperature)
print("Hottest day:", hot_day)
print("Coolest day:", cool_day)
print("Highest-average city index:", highest_temperature_city)
print("Cities above 30 C:", hot_cities)
print("Temperature standard deviation:", temperature_std)
print("Hot or Normal for every temperature:\n", temperature_status)
print(temperature_df)


# ============================================================
# PROJECT 7: BANK TRANSACTION ANALYSIS
# ============================================================
transactions = np.array([
    [5000, 2000, 3000],
    [8000, 1500, 4000],
    [3000, 1000, 2500],
    [10000, 3000, 5000],
    [7000, 2500, 3500]
])

net_balance = transactions[:, 0] - transactions[:, 1]
transaction_status = np.where(
    net_balance > 6000,
    "High",
    np.where(net_balance >= 4000, "Medium", "Low")
)

transaction_df = pd.DataFrame(
    transactions,
    columns=["Deposit", "Withdrawal", "Investment"]
)
transaction_df["Net Balance"] = net_balance
transaction_df["Status"] = transaction_status

print("\nPROJECT 7: BANK TRANSACTION ANALYSIS")
print("Total deposit:", np.sum(transactions[:, 0]))
print("Total withdrawal:", np.sum(transactions[:, 1]))
print("Total investment:", np.sum(transactions[:, 2]))
print("Net balance:", net_balance)
print("Highest-deposit customer index:", np.argmax(transactions[:, 0]))
print("Highest-withdrawal customer index:", np.argmax(transactions[:, 1]))
print("Customers with net balance above 4000:", np.where(net_balance > 4000)[0])
print("Average deposit:", np.mean(transactions[:, 0]))
print("Deposit standard deviation:", np.std(transactions[:, 0]))
print(transaction_df)


# ============================================================
# PROJECT 8: E-COMMERCE CUSTOMER ANALYSIS
# ============================================================
customers = np.array([
    [25, 5, 12000],
    [32, 8, 25000],
    [21, 3, 8000],
    [40, 12, 45000],
    [28, 6, 18000],
    [35, 10, 32000]
])

spending = customers[:, 2]
customer_status = np.where(
    spending >= 30000,
    "Premium",
    np.where(spending >= 15000, "Regular", "Basic")
)

customer_df = pd.DataFrame(
    customers,
    columns=["Age", "Orders", "Total Spending"]
)
customer_df["Status"] = customer_status

print("\nPROJECT 8: E-COMMERCE CUSTOMER ANALYSIS")
print("Average age:", np.mean(customers[:, 0]))
print("Average orders:", np.mean(customers[:, 1]))
print("Average spending:", np.mean(spending))
print("Highest-spending customer index:", np.argmax(spending))
print("Lowest-spending customer index:", np.argmin(spending))
print("Customers spending above 20000:", np.where(spending > 20000)[0])
print("Customers with more than 5 orders:", np.where(customers[:, 1] > 5)[0])
print("Highest-orders customer index:", np.argmax(customers[:, 1]))
print("Spending standard deviation:", np.std(spending))
print("Top three customers:")
print(customer_df.sort_values("Total Spending", ascending=False).head(3))


# ============================================================
# PROJECT 9: IPL PLAYER PERFORMANCE ANALYSIS
# ============================================================
players = np.array([
    [450, 15, 12],
    [520, 18, 15],
    [300, 10, 8],
    [650, 20, 18],
    [400, 14, 10]
])

runs = players[:, 0]
runs_per_match = runs / players[:, 1]
player_status = np.where(
    runs >= 500,
    "Excellent",
    np.where(runs >= 400, "Good", "Average")
)

player_df = pd.DataFrame(players, columns=["Runs", "Matches", "Wickets"])
player_df["Runs per Match"] = runs_per_match
player_df["Status"] = player_status

print("\nPROJECT 9: IPL PLAYER PERFORMANCE ANALYSIS")
print("Average runs:", np.mean(runs))
print("Highest run scorer index:", np.argmax(runs))
print("Lowest run scorer index:", np.argmin(runs))
print("Highest wicket taker index:", np.argmax(players[:, 2]))
print("Runs per match:", runs_per_match)
print("Players with more than 400 runs:", np.where(runs > 400)[0])
print("Players with more than 10 wickets:", np.where(players[:, 2] > 10)[0])
print("Runs standard deviation:", np.std(runs))
print(player_df)


# ============================================================
# PROJECT 10: HOSPITAL PATIENT ANALYSIS
# ============================================================
patients = np.array([
    [25, 120, 80, 72],
    [45, 150, 95, 88],
    [32, 130, 85, 76],
    [60, 170, 110, 92],
    [50, 155, 100, 90]
])

patient_status = np.where(patients[:, 1] > 140, "High", "Normal")
patient_df = pd.DataFrame(
    patients,
    columns=["Age", "Systolic BP", "Diastolic BP", "Heart Rate"]
)
patient_df["BP Status"] = patient_status

print("\nPROJECT 10: HOSPITAL PATIENT ANALYSIS")
print("Average age:", np.mean(patients[:, 0]))
print("Average systolic BP:", np.mean(patients[:, 1]))
print("Average diastolic BP:", np.mean(patients[:, 2]))
print("Highest systolic BP:", np.max(patients[:, 1]))
print("Lowest systolic BP:", np.min(patients[:, 1]))
print("Patients with systolic BP above 140:", np.where(patients[:, 1] > 140)[0])
print("Patients with heart rate above 85:", np.where(patients[:, 3] > 85)[0])
print("Standard deviation of each column:", np.std(patients, axis=0))
print(patient_df)


# ============================================================
# PROJECT 11: MOVIE RATING ANALYSIS
# ============================================================
ratings = np.array([
    [8.5, 120000],
    [7.8, 95000],
    [9.1, 180000],
    [6.9, 70000],
    [8.2, 110000]
])

movie_status = np.where(
    ratings[:, 0] >= 8.5,
    "Excellent",
    np.where(ratings[:, 0] >= 7.5, "Good", "Average")
)
movie_df = pd.DataFrame(ratings, columns=["Rating", "Votes"])
movie_df["Status"] = movie_status

print("\nPROJECT 11: MOVIE RATING ANALYSIS")
print("Average movie rating:", np.mean(ratings[:, 0]))
print("Highest-rated movie index:", np.argmax(ratings[:, 0]))
print("Lowest-rated movie index:", np.argmin(ratings[:, 0]))
print("Movies rated above 8:", np.where(ratings[:, 0] > 8)[0])
print("Movies with more than 100000 votes:", np.where(ratings[:, 1] > 100000)[0])
print("Maximum-votes movie index:", np.argmax(ratings[:, 1]))
print("Rating standard deviation:", np.std(ratings[:, 0]))
print(movie_df.sort_values("Rating", ascending=False))