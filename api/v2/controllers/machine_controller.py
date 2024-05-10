from ninja_extra import (
    api_controller, route, ControllerBase)
from api.v2.exceptions import (
    ConflictException, ServerErrorException,
    BadRequestException)
from api.v2.schemas import (
    MachineSchema, ErrorSchema, SensorSchema)
from api.v2.services import MachineService


@api_controller("/machines")
class MachineController(ControllerBase):
    """
    Controller handling creating of machine instance.
    """
    
    @route.post("/", 
                summary = "Creates a new machine instance.",
                description = "Creates a machine instance then returns a sensor instance.",
                response = {
                    201 : SensorSchema,
                    400 : ErrorSchema,
                    409 : ErrorSchema,
                    500 : ErrorSchema
                })
    def create(self, machine_request : MachineSchema):  
        """
        Endpoint to create a new machine instance and 
        return a new instance of a sensor.

        Args:
            machine_request (MachineSchema): The request data for adding the record for a new machine

        Returns:
            tuple: A tuple containing the status code and response data.
        """
        try:
            response = MachineService.create(machine_request)
            return 201, response
        except BadRequestException as e:
            return 400, ErrorSchema(**e.__dict__)
        except ConflictException as e:
            return 409, ErrorSchema(**e.__dict__)
        except:
            return 500, ErrorSchema(
                **ServerErrorException().__dict__)