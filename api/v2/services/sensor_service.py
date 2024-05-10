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
            raise NotFoundException(
                detail = "Machine instance does not exists.")
        
        if not SensorRepository.is_sensor_exist(machine_code):
            raise NotFoundException(
                detail = "Sensor instance does not exists.")
        
        sensor = SensorRepository.get_sensor(
            machine_code)
        
        if not sensor:
            raise ServerErrorException()
    
        return SensorSchema(**sensor.__dict__).dict()
    
    
    @staticmethod
    def create(machine_code : str):
        
        if not MachineRepository.is_machine_exist(machine_code):
            raise NotFoundException(
                detail = "Machine instance does not exists.")
        
        if SensorRepository.is_sensor_exist(machine_code):
            raise ConflictException(
                detail = "Sensor instance does not exists.")
        
        sensor = SensorRepository.create_sensor(
            machine_code)
        
        if not sensor:
            raise ServerErrorException()
        
        return SensorSchema().dict()
    
    
    @staticmethod
    def update(machine_code : str, sensor_request : SensorSchema):
        
        if not MachineRepository.is_machine_exist(machine_code):
            raise NotFoundException(
                detail = "Machine instance does not exists.")
        
        if not SensorRepository.is_sensor_exist(machine_code):
            raise NotFoundException(
                detail = "Sensor instance does not exists.")
        
        sensor = SensorRepository.update_sensor(
            machine_code, **sensor_request.dict())
        
        if not sensor:
            raise BadRequestException()
        
        return sensor_request.dict()
        
        
    @staticmethod
    def destroy(machine_code : str):
        
        if not MachineRepository.is_machine_exist(machine_code):
            raise NotFoundException(
                detail = "Machine instance does not exists.")
        
        if not SensorRepository.is_sensor_exist(machine_code):
            raise NotFoundException(
                detail = "Sensor instance does not exists.")
        
        if not SensorRepository.delete_sensor(machine_code):    
            raise ServerErrorException()
    
        return {}