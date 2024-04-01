from pydantic import BaseModel


class SensorRequestSchema(BaseModel):
    pass



class SensorResponseSchema(BaseModel):
    is_start : bool
    is_stop : bool
    is_initialized : bool
    counter : int
    timer : int