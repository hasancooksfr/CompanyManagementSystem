from pydantic import BaseModel, Field
from typing import Literal

class createRequest(BaseModel):
    from_date: str = Field(
        pattern=r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
    )
    to_date: str = Field(
        pattern=r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
    )
    reason: str
    leave_type: Literal[
        'casual',
        'sick',
        'unpaid',
        'maternity',
        'paternity'
    ]