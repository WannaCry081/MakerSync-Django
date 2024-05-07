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
    def create(self, machine_request : MachineSchema):  
        try:
            response = MachineService.create(machine_request)
            return response
        except ConflictException as e:
            return 409, ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return 500, ErrorSchema(**e.__dict__)