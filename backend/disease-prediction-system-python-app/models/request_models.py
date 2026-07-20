from typing import Optional

from pydantic import BaseModel


class DiseasePredictionRequest(BaseModel):

    age: int

    bp: float

    glucose: float

    cholesterol: float

    bmi: float

    # Optional vitals
    heart_rate: Optional[float] = 80

    oxygen_level: Optional[float] = 98

    # Optional text inputs
    symptoms: Optional[str] = ""

    doctor_notes: Optional[str] = ""