from api.v2.repositories import (
    SensorRepository, MachineRepository)
from api.v2.exceptions import (
    ConflictException, NotFoundException,
    ServerErrorException)
from api.v2.schemas import (
    SensorSchema)


class SensorService:
    
    @staticmethod
    def retrieve(machine_code : str):
        
        if not MachineRepository.is_machine_exist(machine_code):
            raise NotFoundException()
        
        sensor = SensorRepository.get_sensor(
            machine_code)
        
        if not sensor:
            raise ServerErrorException()
    
        return SensorSchema(**sensor.__dict__).dict()