# Write your MySQL query statement below
select Employees.name , employeeUNI.unique_id
from Employees left join EmployeeUNI on Employees.id = EmployeeUNI.id