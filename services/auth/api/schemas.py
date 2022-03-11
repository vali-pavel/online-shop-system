from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    user_id: int = Field(...)
    user_role: int = Field(...)
    secret_key: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "user_id": 1,
                "user_role": 0,
                "secret_key": "secret key",
            }
        }
