from pydantic import BaseModel


class ImageResult(BaseModel):
    predicted_condition: str
    confidence_score: float
    urgency_level: str
    advice: str
