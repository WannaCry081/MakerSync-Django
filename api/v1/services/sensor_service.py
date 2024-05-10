from api.v1.schemas import (
    SensorSchema, SensorSchema, 
    CreateSensorSchema)
from api.v1.exceptions import (
    BadRequestException, ServerErrorException, 
    NotFoundException, ConflictException)
from api.v1.repositories import SensorRepository


class SensorService:
    
    @staticmethod
    def create(sensor_request : CreateSensorSchema):
        
        machine_code : str = sensor_request.code
        if not SensorRepository.is_sensor_exists(machine_code):
            raise ConflictException(
                detail="Sensors resource already exists.")
        
        if not SensorRepository.create_sensor(machine_code):
            raise ServerErrorException()
        
        return SensorSchema().dict()

    
    @staticmethod
    def retrieve(machine_code : str):
        
        if SensorRepository.is_sensor_exists(machine_code):
            raise NotFoundException(
                detail="Machine does not exists.")
        
        sensor = SensorRepository.get_sensor(machine_code)
        if not sensor:
            raise BadRequestException(
                detail="Invalid machine. Please try again later.")
    
        return SensorSchema(**sensor).dict()
    
    
    @staticmethod
    def update(machine_code : str, sensor_request : SensorSchema): 
        
        if SensorRepository.is_sensor_exists(machine_code):
            raise NotFoundException(
                detail="Sensor not found."
            )
            
        sensor=SensorRepository.update_sensor(machine_code, sensor_request)
        if not sensor: 
            raise BadRequestException(
                detail="Invalid Sensor ID"
            )
       
        return SensorSchema(**sensor_request.dict())
            
    
    @staticmethod
    def destroy(machine_code : str):
        
        if SensorRepository.is_sensor_exists(machine_code):
            raise NotFoundException(
                detail="Sensor not found."
            )
        
        if not SensorRepository.delete_sensor(machine_code):
            raise ServerErrorException()
        
        return True
    