from pydantic import BaseModel, EmailStr
from typing import Optional


# ----- User -----

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True  # for SQLAlchemy -> Pydantic


# ----- Auth -----

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ----- Ticket prediction -----

class TicketIn(BaseModel):
    subject: str
    body: str


class TicketPrediction(BaseModel):
    priority_label: str
    priority_score: float


# Optional: for dashboard later
class TicketLogOut(BaseModel):
    id: int
    subject: str
    body: str
    predicted_priority: str
    predicted_confidence: Optional[float]

    class Config:
        from_attributes = True
