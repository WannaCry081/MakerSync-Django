from pydantic import (
    BaseModel, Field, EmailStr)


class UserSchema(BaseModel):
    
    username : str = Field(
        ..., title = "Username")
    email : EmailStr = Field(
        ..., title = "Email")