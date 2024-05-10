from uuid import UUID
from pydantic import (
    BaseModel, Field, validator)


class CreateSensorSchema(BaseModel):
    code : str = Field(
        ..., title = "Sensor Code")
    
    
    @validator("code")
    def validate_code(cls, value):
        try:
            uuid.UUID(value)
            return value
        except ValueError:
            raise ValueError("Code is not valid.")
    

class SensorSchema(BaseModel):
    is_start : bool = Field(
        title = "Sensor Is Start", default = False)
    is_stop : bool = Field(
        title = "Sensor Is Stop", default = False)
    is_initialize : bool = Field(
        title = "Sensor Is Initialize", default = False)
    counter : int = Field(
        title = "Sensor Counter", default = 0)
    time : int = Field(
        title = "Sensor Time", default = 0)
    temperature : float = Field(
        title = "Sensor Temperature", default = 0.0)