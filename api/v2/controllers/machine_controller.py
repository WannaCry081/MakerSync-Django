from ninja_extra import (
    api_controller, route, ControllerBase)
from api.v2.exceptions import (
    ConflictException, ServerErrorException,
    BadRequestException)
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
        except BadRequestException as e:
            return ErrorSchema(**e.__dict__)
        except ConflictException as e:
            return ErrorSchema(**e.__dict__)
        except:
            return ErrorSchema(
                **ServerErrorException().__dict__)