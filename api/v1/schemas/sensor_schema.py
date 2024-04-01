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



class SensorResponseSchema(BaseModel):
    is_start : bool
    is_stop : bool
    is_initialized : bool
    counter : int
    timer : int