# model.py
from pydantic import BaseModel

class PatientUpdate(BaseModel):
    patient_id: str
    update_message: str
