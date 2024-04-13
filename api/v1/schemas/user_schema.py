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
    is_connect : bool=Field(
        Title="Is Connect",
        default=True
    )


class UserResponseSchema(BaseModel):
    name : str=Field(default="")
    email : str=Field(default="")
    is_connect : bool=Field(default=True)
