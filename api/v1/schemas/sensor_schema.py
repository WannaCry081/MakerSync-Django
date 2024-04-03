from pydantic import BaseModel, Field


class SensorRequestSchema(BaseModel):
    is_start : bool=Field(
        Title="Is Start",
        default=False
    )
    is_stop : bool=Field(
        Title="Is Stop", 
        default=False
    )
    is_initialized : bool=Field(
        Title="Is Initialized", 
        default=False
    )
    counter : int=Field(
        Title="Counter", 
        default=0
    )
    timer : int=Field(
        Title="Timer", 
        default=0
    )
    temperature : float=Field(
        Title="Temperature",
        default=0
    )



class SensorResponseSchema(BaseModel):
    is_start: bool = Field(default=False)
    is_stop: bool = Field(default=False)
    is_initialized: bool = Field(default=False)
    counter: int = Field(default=0)
    timer: int = Field(default=0)
    temperature: float=Field(default=0)