from pydantic import BaseModel, Field

class EmployeeCreate(BaseModel):
    employee_id: str
    name: str
    department_id: str
    email_id: str
    phone_number: int
    date_of_joining: str
    job_title: str
    salary: int
    employment_status: str

class EmployeeUpdate(BaseModel):
    employee_id: str | None = None
    name: str | None = None
    department_id: str | None = None
    email_id: str | None = None
    phone_number: int | None = None
    date_of_joining: str | None = None
    job_title: str | None = None
    salary: int | None = None
    employment_status: str | None=None