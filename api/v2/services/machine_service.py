from api.v2.schemas import (
    MachineSchema, SensorSchema)
from api.v2.exceptions import ( 
    ConflictException, BadRequestException)
from api.v2.repositories import (
    MachineRepository)


class MachineService:
    
    @staticmethod
    def create(machine_request : MachineSchema):
        
        code = machine_request.code 
        if MachineRepository.is_machine_exist(code):
            raise ConflictException(
                detail = "Duplicate machine instance.")
        
        if not MachineRepository.create_machine(code):
            raise BadRequestException() 
        
        return machine_request