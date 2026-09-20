# Attendance Management
This document gives a detailed information about **Attendance Management**. It is the fourth module of Company Management System

It provides basic controls for managing attendance records.

# Features
- Record Check-In Timings
- Record Check-Out Timings
- Calculate late CheckIn/early Checkout seconds
- Mark absent for employees who didn't check-in
- View attendance summary of a single employee
- View attendance data of employee on particular date

# Attendance Information
An attendance record currently contains:
```text
Employee ID
Date (DD-MM-YYYY)
Check in time (HH:MM:SS 24-Hour format)
Check out time (HH:MM:SS 24-Hour format)
Late seconds (Late checkin by how many seconds)
Early seconds (Early checkout by how many seconds)
Mark [Present/Absent]
```

# API Endpoints
## Record check in timings
```http
POST /attendance/check-in/{employee_id}
```

Example request:
```JSON
{
    "date": "20-09-2026",
    "check_in": "08:57:34"
}
```

## Record check out timing
```http
POST /attendance/check-out/{employee_id}
```

Example request:
```JSON
{
    "date": "20-09-2026",
    "check_out": "18:04:29"
}
```

## Mark Absent
```http
POST /attendance/mark-absent
```
This checks attendance records for date (when request was made). If any employee have not checked-in, it marks them as Absent.

## Get attendance summary of an employee
```http
GET /attendance/summary/{employee_id}
```

Example response:
```JSON
{
    "success": true,
    "message": "Fetched attendance summary for employee.",
    "data": {
        "employee_id": "EMP001",
        "active_days": 3,    // Number of working days
        "present_days": 2,   // Number of days when employee was marked as Present
        "absent_days": 1     // Number of days when employee was marked as Absent
    }
}
```

## Get attendance data of employee on date
```http
GET /attendance/{employee_id}?date={date}
```
Returns the attendance record of employee on particular date.

Example response:
```JSON
{
    "employee_id": "EMP001",
    "date": "20-09-2026",
    "check_in": "08:57:34",
    "check_out": "18:04:29",
    "late_seconds": null,
    "early_seconds": null,
    "mark": "Present"
}
```

## Postman Collection
Postman collection for *Attendance Management* can be found [here](https://www.postman.com/hasancooksreal-6713011/workspace/company-management-system/folder/50773921-650d8361-e262-42f9-b1ce-390f0eeb11bf?action=share&creator=50773921). **Please run server first to test all the commands smoothly**.

# Screenshots
## Recording Check-In timing
![Check-In](/assets/attendance-management/check-in.png)

## Recording Check-Out timing
![Check-Out](/assets/attendance-management/check-out.png)

## Mark Absent
![Mark absent](/assets/attendance-management/mark-absent.png)

## Get attendance summary of an employee
![Attendance summary](/assets/attendance-management/attendance-summary.png)

## Get attendance data of an employee on date
![Attendance data](/assets/attendance-management/attendance-data.png)

# Testing
The attendance management feature has been tested for:
- Marking check-in timings
- Marking check-out timings
- Marking employees absent 
- Getting attendance summary of an employee
- Getting attendance data of an employee on date
- Duplicate check-in
- Invalid employee_id