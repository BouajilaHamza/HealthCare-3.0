from pydantic import BaseModel
from fastapi import Form
from enum import Enum
class PatientUpdate(BaseModel):
    patient_id: str = Form(...)
    first_name: str = Form(...)
    last_name: str = Form(...)
    age : int = Form(...)
    gender : str = Form(...)
    illness : str = Form(...)
    message: str = Form(...)
    print(patient_id, message)


class Gender(Enum):
    Male="Male"
    Female="Female"
    
    def __str__(self) -> str:
        return str(self.value)
