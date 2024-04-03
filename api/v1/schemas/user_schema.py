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
    is_active : bool=Field(
        Title="Is Active",
        default=False
    )
    is_connected : bool=Field(
        Title="Is Connected",
        default=False
    )


class UserResponseSchema(BaseModel):
    name : str
    email : str
    is_active : bool
    is_connected : bool
