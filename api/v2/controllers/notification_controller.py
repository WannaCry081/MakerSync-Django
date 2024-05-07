from ninja_extra import (
    api_controller, ControllerBase, route)
from api.v2.schemas import (
    MachineSchema, NotificationSchema)
from api.v2.services import NotificationService


@api_controller("/machines/{machine_id}/notifications")
class NotificationController(ControllerBase):
    
    @route.get("/")
    def list(self, machine_id : MachineSchema):
        pass
    
    
    @route.get("/{notification_id}")
    def retrieve(self, machine_id : MachineSchema, notification_id : int):
        pass
    
    
    @route.post("/")
    def create(self, machine_id : MachineSchema, request : NotificationSchema):
        pass