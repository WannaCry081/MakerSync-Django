from pydantic import (
    BaseModel, Field, EmailStr)


class UserSchema(BaseModel):
    
    username : str = Field(
        ..., title = "Username", default = "")
    email : EmailStr = Field(
        ..., title = "Email", default = "")