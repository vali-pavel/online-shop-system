from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    full_name: str = Field(...)
    phone_number: int = Field(...)
    role_type: int = Field(...)
    password: str = Field(...)


class UserLogin(UserBase):
    password: str


class User(UserBase):
    full_name: str
    phone_number: int
    role_type: int
