from ninja_extra import (
    api_controller, ControllerBase, route)
from api.v2.schemas import (
    NotificationSchema, ErrorSchema)
from api.v2.exceptions import (
    NotFoundException)
from api.v2.services import NotificationService


@api_controller("/machines/{machine_code}/notifications")
class NotificationController(ControllerBase):
    
    @route.get("/")
    def list(self, machine_code : str):
        pass
    
    
    @route.get("/{notification_id}")
    def retrieve(self, machine_code : str, notification_id : int):
        pass
    
    
    @route.post("/")
    def create(self, machine_code : str, request : NotificationSchema):
        pass