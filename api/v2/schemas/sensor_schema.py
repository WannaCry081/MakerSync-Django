from pydantic import (
    BaseModel, Field)


class SensorSchema(BaseModel):

    is_start : bool = Field(
        title = "Is Start", default = False)
    is_stop : bool = Field(
        title = "Is Stop", default = False)
    is_initialize : bool=Field(
        title = "Is Initialize", default = False)
    counter : int = Field(
        title = "Counter", default = 0)
    time : int = Field(
        title = "Time", default = 0)
    temperature : float = Field(
        title = "Temperature", default = 0)