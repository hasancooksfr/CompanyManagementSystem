# Department Management
This document gives a detailed information about **Department Management**. It is the second module of Company Management System

It provides basic CRUD for managing department records.

## Features
- Create Departments
- View all departments
- View department details
- Update department details
- Delete department
- Assign manager to department
- Assign employees to department

## Department Information
A department record currently contains:
```text
Department ID
Name
Description
Manager ID
Status
```

# API Endpoints
## Get all departments
```http
GET /departments/
```
Return a list of departments with basic information.

Example:
```JSON
{
    "success": true,
    "message": "Fetched all departments",
    "data": [
        {
            "department_id": "DEP001",
            "name": "Sales",
            "manager_id": "EMP001"
        }
    ]
}
```

## Get a department details
```http
GET /departments/{department_id}
```
Returns detailed information about a specific department.

## Create a department
```http
POST /departments/
```

Example request:
```JSON
{
    "department_id": "DEP001",
    "name": "Sales",
    "description": "Offline Sales and Marketing department",
    "manager_id": "EMP001",
    "status": "active"
}
```

## Update a department
```http
PUT /departments/{department_id}
```
Updates information for an existing department.

## Delete a department
```http
DELETE /departments/{department_id}
```
Deletes a department record.

## Postman Collection
Postman collection for *Department Management* can be found [here](https://www.postman.com/hasancooksreal-6713011/workspace/company-management-system/folder/50773921-650d8361-e262-42f9-b1ce-390f0eeb11bf?action=share&creator=50773921). **Please run server first to test all the commands smoothly**.

# Screenshots
## Department Creation
![Create department](/assets/department-management/create_department.png)

## Get all departments
![Get all departments](/assets/department-management/get_all_departments.png)

## Get department details
![Get department details](/assets/department-management/get_department_data.png)

## Update department details
![Update department details](/assets/department-management/update_department_data.png)

## Delete department details
![Delete department details](/assets/department-management/detele_department.png)

# Testing
The department management feature has been tested for:
- Creating department records
- Retrieving department records
- Updating department records
- Deleting department records
- Invalid manager_id or department_id errors
- Duplicate department IDs