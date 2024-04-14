from pydantic import BaseModel, Field


class UserRequestSchema(BaseModel):
    name : str=Field(
        Title="Name",
        default=""
    )
    email : str=Field(
        Title="Email",
        default=""
    )


class UserResponseSchema(BaseModel):
    name : str=Field(default="")
    email : str=Field(default="")
