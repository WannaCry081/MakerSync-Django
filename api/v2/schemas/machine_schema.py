import uuid
from pydantic import (
    BaseModel, Field, validator)


class MachineSchema(BaseModel):

    code : str = Field(..., title = "Machine Code")
    
    
    @validator("code")
    def validate_code(cls, value):
        try:
            uuid.UUID(value)
            return value
        except ValueError:
            raise ValueError("Code is not valid.")