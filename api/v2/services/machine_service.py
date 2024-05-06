from api.v2.schemas import (
    MachineSchema, SensorSchema)
from api.v2.exceptions import ( 
    ConflictException, ServerErrorException)


class MachineService:
    
    @staticmethod
    def create(request : MachineSchema):
        
        if MachineRepository.is_machine_exist(request):
            raise ConflictException()
        
        if not MachineRepository.create_machine(request):
            raise ServerErrorException() 
        
        return SensorSchema()