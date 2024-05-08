from pydantic import BaseModel, Field


class CreateSensorSchema(BaseModel):
    code : str = Field(
        ..., title = "Sensor Code")
    

class SensorSchema(BaseModel):
    is_start : bool = Field(
        ..., title = "Sensor Is Start")
    is_stop : bool = Field(
        ..., title = "Sensor Is Stop")
    is_initialize : bool = Field(
        ..., title = "Sensor Is Initialize")
    counter : int = Field(
        ..., title = "Sensor Counter")
    time : int = Field(
        ..., title = "Sensor Time")
    temperature : float=Field(
        ..., title = "Sensor Temperature")