from datetime import date
from pydantic import (
    BaseModel, Field, validator)


class NotificationSchema(BaseModel):
    
    title : str = Field(
        ..., title = "Title") 
    content : str = Field(
        ..., title = "Content")
    date : date = Field(
        ..., title = "Date")
    
    
    @validator("title")
    def validate_title(cls, value):
        
        if len(value) <= 2:
            raise ValueError("Invalid notification title.")
        
        return value