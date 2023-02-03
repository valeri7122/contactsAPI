from datetime import datetime, date
from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    first_name: str = Field(min_length=1, max_length=30)
    last_name: str = Field(min_length=1, max_length=30)
    email: EmailStr
    phone: str = Field(min_length=5, max_length=25)
    birthday: date

class ContactUpdate(ContactModel):
    done: bool

class ContactStatusUpdate(BaseModel):
    done: bool

class ContactResponse(ContactModel):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True