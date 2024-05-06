from datetime import date
from pydantic import (
    BaseModel, Field)


class NotificationSchema(BaseModel):
    
    title : str = Field(
        ..., title = "Title") 
    content : str = Field(
        ..., title = "Content")
    date : date = Field(
        ..., title = "Date")