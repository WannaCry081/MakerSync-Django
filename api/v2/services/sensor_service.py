from api.v2.repositories import (
    SensorRepository, MachineRepository)
from api.v2.exceptions import (
    ConflictException, NotFoundException,
    ServerErrorException, BadRequestException)
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
    
    
    @staticmethod
    def create(machine_code : str):
        
        if not MachineRepository.is_machine_exist(machine_code):
            raise NotFoundException()
        
        sensor = SensorRepository.create_sensor(
            machine_code)
        
        if not sensor:
            raise ServerErrorException()
        
        return SensorSchema().dict()
    
    
    @staticmethod
    def update(machine_code : str, sensor_request : SensorSchema):
        
        if not MachineRepository.is_machine_exist(machine_code):
            raise NotFoundException()
        
        sensor = SensorRepository.update_sensor(
            machine_code, **sensor_request.dict())
        
        if not sensor:
            raise BadRequestException()
        
        return sensor_request.dict()
        