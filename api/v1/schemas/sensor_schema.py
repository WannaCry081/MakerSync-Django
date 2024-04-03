from pydantic import BaseModel, Field


class SensorRequestSchema(BaseModel):
    is_start : bool=Field(
        Title="Is Start",
    )
    is_stop : bool=Field(
        Title="Is Stop", 
    )
    is_initialized : bool=Field(
        Title="Is Initialized", 
    )
    counter : int=Field(
        Title="Counter", 
    )
    timer : int=Field(
        Title="Timer", 
    )
    temperature : float=Field(
        Title="Temperature"
    )



class SensorResponseSchema(BaseModel):
    is_start: bool = Field(default=False)
    is_stop: bool = Field(default=False)
    is_initialized: bool = Field(default=False)
    counter: int = Field(default=0)
    timer: int = Field(default=0)
    temperature: float=Field(default=0)