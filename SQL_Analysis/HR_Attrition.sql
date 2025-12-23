create database hr_analytics;
use hr_analytics;
create table hr_attrition(
	Age INT,
	Attrition VARCHAR(5),
	BusinessTravel VARCHAR(50),
	Department VARCHAR(50),
	DistanceFromHome INT,
	Education INT,
	EducationField VARCHAR(50),
	Gender varchar(10),
	JobRole varchar(50),
	JobLevel INT,
	JobSatisfaction INT,
    MaritalStatus VARCHAR(20),
    MonthlyIncome INT,
    OverTime VARCHAR(5),
    PercentSalaryHike INT,
    TotalWorkingYears INT,
    TrainingTimesLastYear INT,
    WorkLifeBalance INT,
    YearsAtCompany INT,
    YearsInCurrentRole INT,
    YearsSinceLastPromotion INT,
    YearsWithCurrManager INT
);

-- verify data is imported or not 
select count(*) from hr_attrition;
select * from hr_attrition limit 10;

-- Find Total Employees
Select count(*) as total_employee
from hr_attrition;

-- Find Attrition Count 
select Attrition,count(*) as employee_count
from hr_attrition 
group by Attrition;

-- Find Attrition Rate 
SELECT 
ROUND(SUM(CASE WHEN Attrition = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),2) AS attrition_rate_percent
FROM hr_attrition;

-- Find Attrition by department 
select Department,count(*) as attrition_count
from hr_attrition
where Attrition = 'Yes'
group by Department
order by attrition_count desc;

-- Department wise attrition rate 
select Department,count(*) as total_employees,
sum(case when Attrition = 'Yes' then 1 else 0 end) as attrition_count,
round(sum(case when Attrition = 'Yes' then 1 else 0 end)*100/count(*),2) as attrition_rate_percent
from hr_attrition
group by Department;

-- Salary and Compensation Insights

-- Average Monthly Income(Attrition vs Non-Attrition)
select Attrition,round(avg(MonthlyIncome),2) as avg_income
from hr_attrition
group by Attrition;

-- Employees with Income Below Company Average
select count(*) as low_salary_employees
from hr_attrition
where MonthlyIncome < (select avg(MonthlyIncome) from hr_attrition);

-- Attrition count for low salary employees
select count(*) as low_salary_employees
from hr_attrition
where Attrition='Yes' and MonthlyIncome < (select avg(MonthlyIncome) from hr_attrition);

-- Overtime and Work-Life balance 

-- Attrition by OverTime 
select OverTime,count(*) as attrition_count
from hr_attrition 
where Attrition='Yes'
group by OverTime;

-- OverTime Attrition rate
select OverTime,count(*) as total_employees,
sum(case when Attrition='Yes' then 1 else 0 end) as attrition_count,
round(sum(case when Attrition = 'Yes' then 1 else 0 end)*100/count(*),2) as attrition_rate_percent
from hr_attrition
group by OverTime;

-- Attrition Vs Work-Life Balance
select WorkLifeBalance,count(*) as attrition_count
from hr_attrition
where Attrition='Yes'
group by WorkLifeBalance
order by WorkLifeBalance;

-- Job Role & Experience Analysis

-- Attrition by Job Role 
select JobRole,count(*) as attrition_count
from hr_attrition
where Attrition = 'Yes'
group by JobRole
order by attrition_count desc;

-- Average Years at Company 
select Attrition,round(avg(YearsAtCompany),2) as avg_years
from hr_attrition
group by Attrition;

-- Attrition in First 3 years
select count(*) as early_attrition
from hr_attrition
where Attrition='Yes'
and YearsAtCompany <= 3;

-- Satisfaction & Training 

-- Attrition By Job Satisfaction 
select JobSatisfaction,count(*) as attrition_count
from hr_attrition
where Attrition = 'Yes'
group by JobSatisfaction 
order by JobSatisfaction;

-- Attrition Vs Training 
select TrainingTimesLastYear,count(*) attrition_count
from hr_attrition
where Attrition = 'Yes'
group by TrainingTimesLastYear
order by TrainingTimesLastYear;

-- High-Risk Employees Profile

-- High-Risk Employees (HR Focus)
select * from hr_attrition
where Attrition='Yes'
and OverTime='Yes'
AND MonthlyIncome < (select avg(MonthlyIncome) from hr_attrition)
AND JobSatisfaction <=2 ;

-- Department with Highest High-Risk Employees
select Department,count(*) as high_risk_count
from hr_attrition
where OverTime = 'Yes'
AND JobSatisfaction <=2
group by Department
order by high_risk_count desc;

-- Summary Insights 
-- Top 5 Job roles with Highest Attrition
select JobRole,count(*) as attrition_count
from hr_attrition
where Attrition='Yes'
group by JobRole
order by attrition_count desc
limit 5;