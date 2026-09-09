-- ============================================
-- ASSIGNMENT - 5 (MYSQL - 1)
-- EMPLOYEES TABLE
-- ============================================

-- 1. CREATE TABLE

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    emp_age INT,
    emp_department VARCHAR(30),
    emp_salary DECIMAL(10,2),
    emp_city VARCHAR(30)
);


-- ============================================
-- 2. INSERT 10 EMPLOYEES
-- ============================================

INSERT INTO employees
(emp_id, emp_name, emp_age, emp_department, emp_salary, emp_city)
VALUES
(1, 'Amit', 24, 'IT', 45000, 'Lucknow'),
(2, 'Ananya', 28, 'HR', 55000, 'Delhi'),
(3, 'Rahul', 30, 'Finance', 65000, 'Lucknow'),
(4, 'Sneha', 26, 'IT', 70000, 'Delhi'),
(5, 'Arjun', 29, 'HR', 60000, 'Mumbai'),
(6, 'Priya', 23, 'IT', 40000, 'Lucknow'),
(7, 'Vikas', 32, 'Finance', 75000, 'Delhi'),
(8, 'Neha', 27, 'IT', 80000, 'Lucknow'),
(9, 'Riya', 25, 'HR', 50000, 'Mumbai'),
(10, 'Ayesha', 31, 'Finance', 90000, 'Delhi');


-- ============================================
-- 3. DISPLAY ALL EMPLOYEES
-- ============================================

SELECT * FROM employees;


-- ============================================
-- 4. UPDATE SALARY OF ONE EMPLOYEE
-- ============================================

UPDATE employees
SET emp_salary = 60000
WHERE emp_id = 1;


-- ============================================
-- 5. CHANGE ONE EMPLOYEE'S CITY
-- ============================================

UPDATE employees
SET emp_city = 'Kanpur'
WHERE emp_id = 2;


-- ============================================
-- 6. DELETE ONE EMPLOYEE
-- ============================================

-- Run this after completing the other queries
-- if you want to preserve all 10 employees for testing.

DELETE FROM employees
WHERE emp_id = 10;


-- ============================================
-- FILTERING QUERIES
-- ============================================

-- 7. Find employees earning more than 50,000

SELECT *
FROM employees
WHERE emp_salary > 50000;


-- 8. Find employees from IT

SELECT *
FROM employees
WHERE emp_department = 'IT';


-- 9. Find employees from Lucknow

SELECT *
FROM employees
WHERE emp_city = 'Lucknow';


-- 10. Find employees earning between 40,000 and 60,000

SELECT *
FROM employees
WHERE emp_salary BETWEEN 40000 AND 60000;


-- 11. Find employees whose name starts with A

SELECT *
FROM employees
WHERE emp_name LIKE 'A%';


-- 12. Find employees whose name ends with a

SELECT *
FROM employees
WHERE emp_name LIKE '%a';


-- 13. Find employees belonging to IT or HR

SELECT *
FROM employees
WHERE emp_department IN ('IT', 'HR');


-- 14. Find employees older than 25
-- and earning more than 50,000

SELECT *
FROM employees
WHERE emp_age > 25
AND emp_salary > 50000;


-- 15. Find employees whose salary is NULL

SELECT *
FROM employees
WHERE emp_salary IS NULL;


-- 16. Find employees whose salary is NOT NULL

SELECT *
FROM employees
WHERE emp_salary IS NOT NULL;


-- ============================================
-- ORDER BY / GROUP BY / HAVING
-- ============================================

-- 17. Sort employees by salary

SELECT *
FROM employees
ORDER BY emp_salary ASC;


-- 18. Sort employees from highest salary to lowest

SELECT *
FROM employees
ORDER BY emp_salary DESC;


-- 19. Count employees in every department

SELECT emp_department, COUNT(*) AS employee_count
FROM employees
GROUP BY emp_department;


-- 20. Find average salary per department

SELECT emp_department, AVG(emp_salary) AS average_salary
FROM employees
GROUP BY emp_department;


-- 21. Find maximum salary per department

SELECT emp_department, MAX(emp_salary) AS maximum_salary
FROM employees
GROUP BY emp_department;


-- 22. Find departments having more than 5 employees

SELECT emp_department, COUNT(*) AS employee_count
FROM employees
GROUP BY emp_department
HAVING COUNT(*) > 5;


-- 23. Find departments whose average salary
-- is greater than 60,000

SELECT emp_department, AVG(emp_salary) AS average_salary
FROM employees
GROUP BY emp_department
HAVING AVG(emp_salary) > 60000;


-- 24. Sort departments by average salary

SELECT emp_department, AVG(emp_salary) AS average_salary
FROM employees
GROUP BY emp_department
ORDER BY average_salary ASC;


-- 25. Find the number of employees in every city

SELECT emp_city, COUNT(*) AS employee_count
FROM employees
GROUP BY emp_city;


-- 26. Find cities having more than 3 employees

SELECT emp_city, COUNT(*) AS employee_count
FROM employees
GROUP BY emp_city
HAVING COUNT(*) > 3;


-- ============================================
-- AGGREGATE QUERIES
-- ============================================

-- 27. Find total employees

SELECT COUNT(*) AS total_employees
FROM employees;


-- 28. Find total salary

SELECT SUM(emp_salary) AS total_salary
FROM employees;


-- 29. Find average salary

SELECT AVG(emp_salary) AS average_salary
FROM employees;


-- 30. Find maximum salary

SELECT MAX(emp_salary) AS maximum_salary
FROM employees;


-- 31. Find minimum salary

SELECT MIN(emp_salary) AS minimum_salary
FROM employees;


-- 32. Find average salary of IT employees

SELECT AVG(emp_salary) AS average_IT_salary
FROM employees
WHERE emp_department = 'IT';


-- 33. Find highest salary in HR

SELECT MAX(emp_salary) AS highest_HR_salary
FROM employees
WHERE emp_department = 'HR';


-- 34. Find total salary paid to Finance employees

SELECT SUM(emp_salary) AS total_Finance_salary
FROM employees
WHERE emp_department = 'Finance';


-- 35. Find number of employees in Delhi

SELECT COUNT(*) AS Delhi_employees
FROM employees
WHERE emp_city = 'Delhi';


-- 36. Find average salary of employees
-- earning more than 50,000

SELECT AVG(emp_salary) AS average_salary
FROM employees
WHERE emp_salary > 50000;


-- 37. Find department-wise total salary

SELECT emp_department, SUM(emp_salary) AS total_salary
FROM employees
GROUP BY emp_department;


-- 38. Find department-wise average salary

SELECT emp_department, AVG(emp_salary) AS average_salary
FROM employees
GROUP BY emp_department;


-- 39. Find department with the highest average salary

SELECT emp_department, AVG(emp_salary) AS average_salary
FROM employees
GROUP BY emp_department
ORDER BY average_salary DESC
LIMIT 1;


-- 40. Find department with the highest total salary

SELECT emp_department, SUM(emp_salary) AS total_salary
FROM employees
GROUP BY emp_department
ORDER BY total_salary DESC
LIMIT 1;


-- 41. Find city-wise employee count

SELECT emp_city, COUNT(*) AS employee_count
FROM employees
GROUP BY emp_city;