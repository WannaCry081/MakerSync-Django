from api.v1.schemas import (
    SensorSchema, CreateSensorSchema)
from api.v1.exceptions import (
    BadRequestException, ServerErrorException, 
    NotFoundException, ConflictException)
from api.v1.repositories import MachineRepository


class MachineService:
    
    @staticmethod
    def create(sensor_request : CreateSensorSchema):
        
        machine_code : str = sensor_request.code
        if MachineRepository.is_machine_exists(machine_code):
            raise ConflictException(
                detail = "Duplicate machine instance.")
        
        if not MachineRepository.create_sensor(machine_code):
            raise BadRequestException()
        
        return SensorSchema()

    
    @staticmethod
    def retrieve(machine_code : str):
        
        if not MachineRepository.is_machine_exists(machine_code):
            raise NotFoundException(
                detail="Machine instance does not exists.")
        
        sensor = MachineRepository.get_sensor(machine_code)
        if not sensor:
            raise BadRequestException()
    
        return SensorSchema(**sensor)
    
    
    @staticmethod
    def update(machine_code : str, sensor_request : SensorSchema): 
        
        if not MachineRepository.is_machine_exists(machine_code):
            raise NotFoundException(
                detail="Machine instance does not exists.")
            
        sensor = MachineRepository.update_sensor(
            machine_code, **sensor_request.dict())
        
        if not sensor: 
            raise BadRequestException()

        return sensor_request
            
    
    @staticmethod
    def destroy(machine_code : str):
        
        if not MachineRepository.is_machine_exists(machine_code):
            raise NotFoundException(
                detail = "Machine instance does not exists.")
        
        if not MachineRepository.delete_sensor(machine_code):
            raise ServerErrorException()
        
        return True
    