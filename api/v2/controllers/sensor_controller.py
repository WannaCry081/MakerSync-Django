from ninja_extra import (
    api_controller, ControllerBase, route)
from api.v2.schemas import (
    MachineSchema, SensorSchema)
from api.v2.services import (
    SensorService)
from api.v2.exceptions import (
    ConflictException, ServerErrorException,
    NotFoundException)
from api.v2.schemas import ErrorSchema


@api_controller("/machines/{machine_code}/sensors")
class SensorController(ControllerBase):
    
    @route.get("/")
    def retrieve(self, machine_code : str):
        try:
            response = SensorService.retrieve(machine_code)
            return response
        except NotFoundException as e:
            return ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return ErrorSchema(**e.__dict__)
            
    
    @route.post("/")
    def create(self, machine_code : str):
        try:
            response = SensorService.create(machine_code)
            return response
        except NotFoundException as e:
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
        except NotFoundException as e:
            return ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return ErrorSchema(**e.__dict__)
    
    
    @route.delete("/")
    def destroy(self, machine_code : str):
        try:
            response = SensorService.destroy(machine_code)
            return response
        except NotFoundException as e:
            return ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return ErrorSchema(**e.__dict__)