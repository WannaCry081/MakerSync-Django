from ninja_extra import (
    api_controller, ControllerBase, route)
from api.v2.schemas import (
    MachineSchema, NotificationSchema)


@api_controller("/machines/{code}/notifications")
class NotificationController(ControllerBase):
    
    @route.get("/")
    def list(self, code : MachineSchema):
        pass
    
    
    @route.get("/{notification_id}")
    def retrieve(self, code : MachineSchema, notification_id : int):
        pass
    
    
    @route.post("/")
    def create(self, code : MachineSchema, request : NotificationSchema):
        pass