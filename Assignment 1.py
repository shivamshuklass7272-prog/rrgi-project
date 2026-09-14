import numpy as np
import pandas as pd

def project_1_student_performance():
    marks = np.array([
        [85, 80, 90], [70, 75, 65], [92, 88, 95],
        [60, 72, 68], [78, 82, 80]
    ])
    total = np.sum(marks, axis=1)
    average = np.mean(marks, axis=1)
    status = np.where(average >= 40, "Pass", "Fail")
    result = pd.DataFrame({
        "Python": marks[:, 0], "SQL": marks[:, 1],
        "Machine Learning": marks[:, 2], "Total": total,
        "Average": average, "Status": status
    })
    print("\nPROJECT 1: STUDENT PERFORMANCE ANALYSIS")
    print("Marks:\n", marks)
    print("Total marks:", total)
    print("Average marks:", average)
    print("Average per subject:", np.mean(marks, axis=0))
    print("Highest per subject:", np.max(marks, axis=0))
    print("Lowest per subject:", np.min(marks, axis=0))
    print("Students above average 80:", np.where(average > 80)[0])
    print("Highest-performing student index:", np.argmax(average))
    print("Standard deviation per subject:", np.std(marks, axis=0))
    print(result)
    return result


def project_2_employee_salary():
    salary = np.array([
        [25000, 2, 80], [45000, 5, 90], [30000, 3, 75],
        [60000, 8, 95], [35000, 4, 85]
    ])
    result = pd.DataFrame(salary, columns=["Salary", "Experience", "Performance"])
    result["Salary Status"] = np.where(result["Salary"] > 40000, "High Salary", "Low Salary")
    print("\nPROJECT 2: EMPLOYEE SALARY ANALYSIS")
    print("Average salary:", np.mean(salary[:, 0]))
    print("Highest salary:", np.max(salary[:, 0]))
    print("Lowest salary:", np.min(salary[:, 0]))
    print("Average experience:", np.mean(salary[:, 1]))
    print("Salary > 40000:\n", result[result["Salary"] > 40000])
    print("Performance > 80:\n", result[result["Performance"] > 80])
    print("Highest-performance employee index:", np.argmax(salary[:, 2]))
    print("Salary standard deviation:", np.std(salary[:, 0]))
    print(result)


def project_3_sales_performance():
    sales = np.array([
        [12000, 15000, 18000], [10000, 14000, 16000], [18000, 20000, 22000],
        [9000, 12000, 15000], [15000, 17000, 19000]
    ])
    total_sales = np.sum(sales, axis=1)
    average_sales = np.mean(sales, axis=1)
    result = pd.DataFrame(sales, columns=["January", "February", "March"])
    result["Total Sales"] = total_sales
    result["Average Sales"] = average_sales
    result["Category"] = np.where(
        average_sales >= 18000, "Excellent",
        np.where(average_sales >= 14000, "Good", "Needs Improvement")
    )
    print("\nPROJECT 3: SALES PERFORMANCE ANALYSIS")
    print("Total sales per salesperson:", total_sales)
    print("Average sales per salesperson:", average_sales)
    print("Highest sales per month:", np.max(sales, axis=0))
    print("Lowest sales per month:", np.min(sales, axis=0))
    print("Highest total-sales salesperson index:", np.argmax(total_sales))
    print("Average sales above 15000:", np.where(average_sales > 15000)[0])
    print("Company sales per month:", np.sum(sales, axis=0))
    print("Monthly-sales standard deviation:", np.std(sales, axis=0))
    print(result)


def project_4_attendance():
    attendance = np.array([
        [90, 85, 95, 88], [75, 80, 70, 78], [95, 92, 98, 96],
        [65, 70, 72, 68], [85, 88, 90, 87]
    ])
    average_student = np.mean(attendance, axis=1)
    result = pd.DataFrame(attendance, columns=["Python", "Java", "SQL", "ML"])
    result["Average Attendance"] = average_student
    result["Status"] = np.where(average_student >= 75, "Eligible", "Not Eligible")
    print("\nPROJECT 4: STUDENT ATTENDANCE ANALYSIS")
    print("Average attendance per student:", average_student)
    print("Average attendance per subject:", np.mean(attendance, axis=0))
    print("Highest attendance per subject:", np.max(attendance, axis=0))
    print("Lowest attendance per subject:", np.min(attendance, axis=0))
    print("Students above 80%:", np.where(average_student > 80)[0])
    print("Highest-average student index:", np.argmax(average_student))
    print("Attendance standard deviation:", np.std(attendance, axis=0))
    print(result)


def project_5_product_sales():
    sales = np.array([
        [100, 120, 150], [80, 100, 130], [150, 160, 180],
        [70, 90, 110], [120, 140, 160]
    ])
    total_sales = np.sum(sales, axis=1)
    average_sales = np.mean(sales, axis=1)
    result = pd.DataFrame({
        "Product": ["Product 1", "Product 2", "Product 3", "Product 4", "Product 5"],
        "Total Sales": total_sales,
        "Average Sales": average_sales,
    })
    result["Classification"] = np.where(average_sales > 120, "High", "Low")
    print("\nPROJECT 5: PRODUCT SALES ANALYSIS")
    print("Best-selling product index:", np.argmax(total_sales))
    print("Worst-selling product index:", np.argmin(total_sales))
    print("Highest sales per month:", np.max(sales, axis=0))
    print("Lowest sales per month:", np.min(sales, axis=0))
    print("Products with average sales > 120:", np.where(average_sales > 120)[0])
    print("Total sales per month:", np.sum(sales, axis=0))
    print("Sales standard deviation:", np.std(sales, axis=0))
    print(result.sort_values("Total Sales", ascending=False))


def project_6_weather():
    temperature = np.array([
        [32, 34, 35, 33, 31], [28, 30, 31, 29, 27],
        [35, 36, 38, 37, 34], [25, 27, 29, 28, 26]
    ])
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    average_city = np.mean(temperature, axis=1)
    average_day = np.mean(temperature, axis=0)
    result = pd.DataFrame(temperature, columns=days)
    result.insert(0, "City", ["City 1", "City 2", "City 3", "City 4"])
    result["Average Temperature"] = average_city
    result["Classification"] = np.where(temperature.max(axis=1) >= 35, "Hot", "Normal")
    print("\nPROJECT 6: WEATHER DATA ANALYSIS")
    print("Average temperature per city:", average_city)
    print("Maximum per city:", np.max(temperature, axis=1))
    print("Minimum per city:", np.min(temperature, axis=1))
    print("Hottest day:", days[np.argmax(average_day)])
    print("Coolest day:", days[np.argmin(average_day)])
    print("Highest-average city index:", np.argmax(average_city))
    print("Cities above 30 C:", np.where(average_city > 30)[0])
    print("Temperature standard deviation:", np.std(temperature))
    print(result)


def project_7_bank_transactions():
    transactions = np.array([
        [5000, 2000, 3000], [8000, 1500, 4000], [3000, 1000, 2500],
        [10000, 3000, 5000], [7000, 2500, 3500]
    ])
    net_balance = transactions[:, 0] - transactions[:, 1]
    result = pd.DataFrame(transactions, columns=["Deposit", "Withdrawal", "Investment"])
    result["Net Balance"] = net_balance
    result["Category"] = np.where(
        net_balance > 6000, "High",
        np.where(net_balance >= 4000, "Medium", "Low")
    )
    print("\nPROJECT 7: BANK TRANSACTION ANALYSIS")
    print("Total deposit:", np.sum(transactions[:, 0]))
    print("Total withdrawal:", np.sum(transactions[:, 1]))
    print("Total investment:", np.sum(transactions[:, 2]))
    print("Net balance:", net_balance)
    print("Highest-deposit customer index:", np.argmax(transactions[:, 0]))
    print("Highest-withdrawal customer index:", np.argmax(transactions[:, 1]))
    print("Net balance above 4000:", np.where(net_balance > 4000)[0])
    print("Average deposit:", np.mean(transactions[:, 0]))
    print("Deposit standard deviation:", np.std(transactions[:, 0]))
    print(result)


def project_8_ecommerce():
    customers = np.array([
        [25, 5, 12000], [32, 8, 25000], [21, 3, 8000],
        [40, 12, 45000], [28, 6, 18000], [35, 10, 32000]
    ])
    spending = customers[:, 2]
    result = pd.DataFrame(customers, columns=["Age", "Orders", "Total Spending"])
    result["Category"] = np.where(
        spending >= 30000, "Premium",
        np.where(spending >= 15000, "Regular", "Basic")
    )
    print("\nPROJECT 8: E-COMMERCE CUSTOMER ANALYSIS")
    print("Average age:", np.mean(customers[:, 0]))
    print("Average orders:", np.mean(customers[:, 1]))
    print("Average spending:", np.mean(spending))
    print("Highest-spending customer index:", np.argmax(spending))
    print("Lowest-spending customer index:", np.argmin(spending))
    print("Spending above 20000:", np.where(spending > 20000)[0])
    print("Orders above 5:", np.where(customers[:, 1] > 5)[0])
    print("Highest-orders customer index:", np.argmax(customers[:, 1]))
    print("Spending standard deviation:", np.std(spending))
    print("Top three customers:\n", result.sort_values("Total Spending", ascending=False).head(3))


def project_9_ipl():
    players = np.array([
        [450, 15, 12], [520, 18, 15], [300, 10, 8],
        [650, 20, 18], [400, 14, 10]
    ])
    runs = players[:, 0]
    result = pd.DataFrame(players, columns=["Runs", "Matches", "Wickets"])
    result["Runs per Match"] = runs / players[:, 1]
    result["Category"] = np.where(
        runs >= 500, "Excellent", np.where(runs >= 400, "Good", "Average")
    )
    print("\nPROJECT 9: IPL PLAYER PERFORMANCE ANALYSIS")
    print("Average runs:", np.mean(runs))
    print("Highest run scorer index:", np.argmax(runs))
    print("Lowest run scorer index:", np.argmin(runs))
    print("Highest wicket taker index:", np.argmax(players[:, 2]))
    print("Players above 400 runs:", np.where(runs > 400)[0])
    print("Players above 10 wickets:", np.where(players[:, 2] > 10)[0])
    print("Runs standard deviation:", np.std(runs))
    print(result)


def project_10_hospital():
    patients = np.array([
        [25, 120, 80, 72], [45, 150, 95, 88], [32, 130, 85, 76],
        [60, 170, 110, 92], [50, 155, 100, 90]
    ])
    result = pd.DataFrame(patients, columns=["Age", "Systolic BP", "Diastolic BP", "Heart Rate"])
    result["BP Status"] = np.where(result["Systolic BP"] > 140, "High", "Normal")
    print("\nPROJECT 10: HOSPITAL PATIENT ANALYSIS")
    print("Average age:", np.mean(patients[:, 0]))
    print("Average systolic BP:", np.mean(patients[:, 1]))
    print("Average diastolic BP:", np.mean(patients[:, 2]))
    print("Highest systolic BP:", np.max(patients[:, 1]))
    print("Lowest systolic BP:", np.min(patients[:, 1]))
    print("Systolic BP above 140:", np.where(patients[:, 1] > 140)[0])
    print("Heart rate above 85:", np.where(patients[:, 3] > 85)[0])
    print("Standard deviation per column:", np.std(patients, axis=0))
    print(result)


def project_11_movies():
    ratings = np.array([
        [8.5, 120000], [7.8, 95000], [9.1, 180000],
        [6.9, 70000], [8.2, 110000]
    ])
    result = pd.DataFrame(ratings, columns=["Rating", "Votes"])
    result["Category"] = np.where(
        result["Rating"] >= 8.5, "Excellent",
        np.where(result["Rating"] >= 7.5, "Good", "Average")
    )
    print("\nPROJECT 11: MOVIE RATING ANALYSIS")
    print("Average rating:", np.mean(ratings[:, 0]))
    print("Highest rating:", np.max(ratings[:, 0]))
    print("Lowest rating:", np.min(ratings[:, 0]))
    print("Movies rated above 8:\n", result[result["Rating"] > 8])
    print("Movies with votes above 100000:\n", result[result["Votes"] > 100000])
    print("Maximum-votes movie index:", np.argmax(ratings[:, 1]))
    print("Rating standard deviation:", np.std(ratings[:, 0]))
    print(result.sort_values("Rating", ascending=False))


def run_all_projects():
    project_1_student_performance()
    project_2_employee_salary()
    project_3_sales_performance()
    project_4_attendance()
    project_5_product_sales()
    project_6_weather()
    project_7_bank_transactions()
    project_8_ecommerce()
    project_9_ipl()
    project_10_hospital()
    project_11_movies()


PROJECTS = {
    "1": project_1_student_performance,
    "2": project_2_employee_salary,
    "3": project_3_sales_performance,
    "4": project_4_attendance,
    "5": project_5_product_sales,
    "6": project_6_weather,
    "7": project_7_bank_transactions,
    "8": project_8_ecommerce,
    "9": project_9_ipl,
    "10": project_10_hospital,
    "11": project_11_movies,
}


def main():
    print("\nProjects 1-11: choose one | 0: run all")
    choice = input("Project number: ").strip()
    if choice == "0":
        run_all_projects()
    elif choice in PROJECTS:
        PROJECTS[choice]()
    else:
        print("Invalid project number.")


if __name__ == "__main__":
    main()