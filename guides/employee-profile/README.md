# Employee Profile
This document gives a detailed information about **Employee Profile**. It is the fifth module of Company Management System.

It helps retieve almost all information about employee in a single request.

# Features
It only has 2 ways to retieve profile:
- Complete profile with most information
- All payrolls generated or paid towards employee

# Profile Information
Complete profile request returns:
```text
Employee ID
Name
Email ID
Phone Number
Date of Joining
Job Title
Department
Department ID
Manager: 
    Manager ID
    Manager Name
    Manager Email ID
Salary
Attendance:
    Working Days
    Present Days
    Absent Days
Employment Status
```

Payroll request returns:
```text
Data: (Same structure for all payrolls)
    Payroll ID,
    Employee ID,
    Month,
    Basic Salary,
    Allowances,
    Deductions,
    Net Salary,
    Status
Pagination: (All payrolls are not returned in single request, they are limited by paginations)
    Page (Current Page)
    Limit (How many records in a single page)
    Total Records (Total payrolls)
    Total Pages (Number of pages)
```

# API Endpoints
## Fetch Employee Profile
```http
GET /profile/{employee_id}
```
Returns complete profile (as shown in Profile Information).

## Fetch Payroll records
```http
GET /profile/{employee_id}/payroll?page={page}&limit={limit}
```
Returns payroll records (as shown in Profile Information).
Pagination is set default as `page` to `1` and `limit` to `10` which means to show page 1 and limit 10 records per page. So, `?page={page}&limit={limit}` is completely optional.

## Postman Collection
Postman collection for *Employee Profile* can be found [here](https://www.postman.com/hasancooksreal-6713011/workspace/company-management-system/folder/50773921-650d8361-e262-42f9-b1ce-390f0eeb11bf?action=share&creator=50773921). **Please run server first to test all the commands smoothly**.

# Screenshots
## Fetch Employee Profile
![Employee Profile](/assets/employee-profile/employee-profile.png)

## Fetch Payroll records
![Payroll records](/assets/employee-profile/payrolls.png)

# Testing
The employee profile feature has been tested for:
- Fetching Employee profile
- Fetching manager details
- Fetching attendance records
- Fetching payroll records
- Invalid employee_id