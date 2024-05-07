from ninja_extra import (
    api_controller, ControllerBase, route)
from api.v2.schemas import (
    NotificationSchema, ErrorSchema)
from api.v2.exceptions import (
    NotFoundException, ServerErrorException)
from api.v2.services import NotificationService


@api_controller("/machines/{machine_code}/notifications")
class NotificationController(ControllerBase):
    
    @route.get("/")
    def list(self, machine_code : str):
        try: 
            response = NotificationService.list(machine_code)
            return response
        except NotFoundException as e:
            return ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return ErrorSchema(**e.__dict__)
    
    
    @route.get("/{notification_id}")
    def retrieve(self, machine_code : str, notification_id : int):
        try:
            response = NotificationService.retrieve(
                machine_code, notification_id)
            return response
        except NotFoundException as e:
            return ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return ErrorSchema(**e.__dict__)

    
    @route.post("/")
    def create(self, machine_code : str, request : NotificationSchema):
        pass