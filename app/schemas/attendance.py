from pydantic import BaseModel, Field
from datetime import time

class CheckIn(BaseModel):
    date: str = Field(
        pattern=r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
    )
    check_in: time

class CheckOut(BaseModel):
    date: str = Field(
        pattern = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
    )
    check_out: time