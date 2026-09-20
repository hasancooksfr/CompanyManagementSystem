# CompanyManagementSystem
The **Company Management System** is a web-based management system designed to help companies manage employees, departments, attendance, leave, payroll and other internal operations from a centralised platform. 

The project is being developed using **FastAPI** and **MongoDB**, with additional modules planned throughout the development period.

## Features
This system currently includes the following modules:
- Employee Management
- Department Management
- Payroll Management
- Attendance Management
- Employee Profiles

Additional modules and improvements will be added throughout development.

## Tech Stack
| Technology | Purpose |
|------------|---------|
| Python | Backend Language |
| FastAPI | REST API framework |
| MongoDB | Database |
| PyMongo | MongoDB integration | 
| Uvicorn | Development Server |
| python-dotenv | Environment variable management |

## Module Guides
Detailed documentation for each module is available in the `/guides` dictionary.

| Module | Guide |
|--------|-------|
| Employee Management | [Employee Management Guide](/guides/employee-management/) |
| Department Management | [Department Management Guide](/guides/department-management/) |
| Payroll Management | [Payroll Management Guide](/guides/payroll-management/) |
| Attendance Management | [Attendance Management Guide](/guides/attendance-management/) |
| Employee Profile | [Employee Profile Guide](/guides/employee-profile/) |

> This list can be updated as new modules are added.


## Running the project
### 1. Clone the repository
```bash
git clone https://github.com/hasancooksfr/CompanyManagementSystem
cd CompanyManagementSystem
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
Create an `.env` file:
```env
MONGO_URI=your_mongodb_connection_string
```

### 4. Start the server
```bash
cd app
uvicorn main:app --reload
```

The API will be available at:
```
http://127.0.0.1:8000
```

## Database
This project uses **MongoDB** for data storage.

The system currently uses separate collections for different areas of applications, including:
```text
employees
departments
attendance
salary_structure
payroll
```
Each module is responsible for managing its own related data while using identifiers such as `employee_id` and `department_id` to connect records.

## Frontend

The frontend is currently being developed separately by a team member on the `frontend` branch.

The frontend is still under active development and is not yet ready to be merged into `main` for the current ship.

The currently shipped version therefore focuses on the backend and API functionality. The `frontend` branch will be integrated into `main` branch once the frontend development and testing are complete.