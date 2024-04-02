from api.v1.schemas import SensorRequestSchema, SensorResponseSchema
from api.v1.repositories import SensorRepository
from api.v1.exceptions import BadRequestException, ServerErrorException, NotFoundException


class SensorService:
    
    @staticmethod
    def create(sensor_id : str, sensor_request : SensorRequestSchema):
        
        if not SensorRepository.is_sensor_exists:
            raise BadRequestException(
                detail="Duplicate instance of sensor exists."
            )
        
        if SensorRepository.create_sensor(sensor_id, sensor_request):
            return SensorResponseSchema(**sensor_request.dict())
        
        raise ServerErrorException()
    
    
    @staticmethod
    def retrieve(sensor_id : str):
        
        if not SensorRepository.is_sensor_exists:
            raise BadRequestException(
                detail="Duplicate instance of sensor exists."
            )
        
        sensor=SensorRepository.get_sensor(sensor_id)
        if not sensor:
            raise NotFoundException(
                detail="Sensor not found."
            )
    
        return sensor