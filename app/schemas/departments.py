from pydantic import BaseModel, Field

class DepartmentCreate(BaseModel):
    department_id: str
    name: str
    description: str
    manager_id: str
    status: str

class DepartmentUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    manager_id: str | None = None
    status: str | None = None