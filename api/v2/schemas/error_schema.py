from pydantic import (
    BaseModel, Field)


class ErrorSchema(BaseModel):
    
    detail : str = Field(
        ..., title = "Error Detail")
    status  : int = Field(
        ..., title = "Error Status Code")