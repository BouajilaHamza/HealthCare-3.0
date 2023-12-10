from pydantic import BaseModel
from fastapi import Form

class PatientUpdate(BaseModel):
    patient_id: str = Form(...)
    update_message: str = Form(...)
    
    @classmethod
    def as_form(cls, patient_id: str = Form(...), update_message: str = Form(...)) -> 'PatientUpdate':
        return cls(patient_id=patient_id, update_message=update_message)
