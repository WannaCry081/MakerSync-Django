from api.v2.schemas import (
    MachineSchema, SensorSchema)
from api.v2.exceptions import ( 
    ConflictException, ServerErrorException)
from api.v2.repositories import (
    MachineRepository)


class MachineService:
    
    @staticmethod
    def create(machine_request : MachineSchema):
        
        code = machine_request.code 
        if MachineRepository.is_machine_exist(code):
            raise ConflictException()
        
        if not MachineRepository.create_machine(code):
            raise ServerErrorException() 
        
        return SensorSchema()