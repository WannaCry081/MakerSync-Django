from datetime import datetime
from pydantic import (
    BaseModel, Field, validator)


class CreateNotificationSchema(BaseModel):
    
    title : str = Field(
        ..., title = "Notification Title") 
    content : str = Field(
        ..., title = "Notification Content")
    
    
    @validator("title")
    def validate_title(cls, value : str):
        
        if len(value) <= 2:
            raise ValueError("Invalid notification title.")
        
        return value
    
    
    @validator("content")
    def validate_content(cls, value : str):
        space_count = len(value.split(" "))
        
        if space_count <= 5:
            raise ValueError("Invalid notification content.")
        
        return value
    
    
class NotificationSchema(BaseModel):
    id : int = Field(
        ..., title = "Notification ID")
    title : str = Field(
        ..., title = "Notification Title") 
    content : str = Field(
        ..., title = "Notification Content")
    created : datetime = Field(
        ..., title = "Notification Date")
    