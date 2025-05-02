from datetime import date
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class SurveyBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = Field(None, max_length=2)
    zip: Optional[str] = None
    phone: Optional[str] = None
    date_of_survey: Optional[date] = None
    liked_most: Optional[str] = None
    interested_in: Optional[str] = None
    likelihood: Optional[str] = None

class SurveyCreate(SurveyBase):
    pass

class SurveyUpdate(SurveyBase):
    id: int

class SurveyRead(SurveyBase):
    id: int

    class Config:
        from_attributes = True
