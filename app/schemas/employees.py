from pydantic import BaseModel, Field

class EmployeeCreate(BaseModel):
    employee_id: str
    name: str
    department: str
    email_id: str
    phone_number: int
    date_of_joining: str
    job_title: str
    salary: int
    employement_status: str