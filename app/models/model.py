from pydantic import BaseModel
from app.schemas.update_patient_schema import Gender
import numpy as np
class PatientUpdate(BaseModel):
    patient_id: str
    first_name: str
    last_name: str
    age : int
    gender : Gender
    illness : str
    message: str
