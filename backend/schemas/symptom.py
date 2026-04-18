from pydantic import BaseModel, Field


class SymptomInput(BaseModel):
    symptoms: list[str] = Field(min_length=1)
    age: int
    gender: str


class SymptomResult(BaseModel):
    predicted_condition: str
    confidence_score: float
    urgency_level: str
    recommended_specialist: str
