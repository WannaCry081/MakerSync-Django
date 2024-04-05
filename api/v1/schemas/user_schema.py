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
    is_connected : bool=Field(
        Title="Is Connected",
        default=False
    )


class UserResponseSchema(BaseModel):
    name : str=Field(default="")
    email : str=Field(default="")
    is_connected : bool=Field(default=False)
