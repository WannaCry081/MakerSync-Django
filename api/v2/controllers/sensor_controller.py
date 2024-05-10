from ninja_extra import (
    api_controller, ControllerBase, route)
from api.v2.schemas import (
    MachineSchema, SensorSchema)
from api.v2.services import (
    SensorService)
from api.v2.exceptions import (
    ConflictException, ServerErrorException,
    NotFoundException, BadRequestException)
from api.v2.schemas import ErrorSchema


@api_controller("/machines/{machine_code}/sensors")
class SensorController(ControllerBase):
    """
    Controller handling the Sensor instance.
    """
    
    @route.get("/",
               summary = "Retrieves a sensor instance.",
               description = "Retrieves a sensor instance based on the path parameter inputted",
               response = {
                   200 : SensorSchema,
                   404 : ErrorSchema,
                   500 : ErrorSchema
               })
    def retrieve(self, machine_code : str):
        """
        Endpoint to retrieves a sensor instance based on the machine code.

        Args:
            machine_code (str): The ID of the machine.

        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            response = SensorService.retrieve(machine_code)
            return 200, response
        except NotFoundException as e:
            return 404, ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return 500, ErrorSchema(**e.__dict__)
            
    
    @route.post("/")
    def create(self, machine_code : str):
        try:
            response = SensorService.create(machine_code)
            return response
        except NotFoundException as e:
            return ErrorSchema(**e.__dict__)
        except ConflictException as e:
            return ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return ErrorSchema(**e.__dict__)
    
    
    @route.put("/")
    def update(self, machine_code : str, 
               sensor_request : SensorSchema):
        try:
            response = SensorService.update(
                machine_code, sensor_request)
            return response
        except BadRequestException as e:
            return ErrorSchema(**e.__dict__)
        except NotFoundException as e:
            return ErrorSchema(**e.__dict__)
        except:
            return ErrorSchema(
                **ServerErrorException().__dict__)
    
    
    @route.delete("/")
    def destroy(self, machine_code : str):
        try:
            response = SensorService.destroy(machine_code)
            return response
        except NotFoundException as e:
            return ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return ErrorSchema(**e.__dict__)