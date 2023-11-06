from pydantic import BaseModel, Field, EmailStr


class OwnerModel(BaseModel):
    email: EmailStr


class OwnerResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True
