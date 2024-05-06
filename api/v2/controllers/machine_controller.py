from ninja_extra import (
    api_controller, route, ControllerBase)
from api.v2.exceptions import (
    ConflictException, ServerErrorException)
from api.v2.schemas import (
    MachineSchema, ErrorSchema)
from api.v2.services import MachineService


@api_controller("/machines")
class MachineController(ControllerBase):
    
    @route.post("/")
    def create(self, request : MachineSchema):  
        try:
            response = MachineService.create(request)
            return 201, response
        except ConflictException as e:
            return 409, ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return 500, ErrorSchema(**e.__dict__)