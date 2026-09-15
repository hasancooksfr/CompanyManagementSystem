from pydantic import BaseModel, Field
from typing import Dict

class SalaryStructure(BaseModel):
    employee_id: str
    basic_salary: float = Field(gt=0)
    allowances: Dict[str, float] = Field(default_factory=dict)
    deductions: Dict[str, float] = Field(default_factory=dict)

class SalaryStructureUpdate(BaseModel):
    basic_salary: float = Field(gt=0)
    allowances: Dict[str, float] = Field(default_factory=dict)
    deductions: Dict[str, float] = Field(default_factory=dict)

class PayrollGenerate(BaseModel):
    month: str