from ninja_extra import route, api_controller, ControllerBase
from api.v1.schemas import SensorRequestSchema, SensorResponseSchema, ErrorResponseSchema
from api.v1.services.sensor_service import SensorService
from api.v1.exceptions import BadRequestException, ServerErrorException


@api_controller("/sensor")
class SensorController(ControllerBase):
    
    @route.post("/{sensor_id}", response={
        201 : SensorResponseSchema, 
        400 : ErrorResponseSchema,
        500 : ErrorResponseSchema
    })
    def create(self, sensor_id : str, sensor_request : SensorRequestSchema):
        try:
            response=SensorResponseSchema(**sensor_request.dict())
            return 201, response
        except BadRequestException as e:
            return 404, ErrorResponseSchema(
                status=e.status_code, 
                detail=e.detail
            )
        except ServerErrorException as e:
            return 500, ErrorResponseSchema(
                status=e.status_code, 
                detail=e.detail
            )
    
    @route.get("/{sensor_id}")
    def retrieve(self, sensor_id : str):
        pass
    
    @route.put("/{sensor_id}")        
    def update(self, sensor_id : str, 
               sensor_request : SensorRequestSchema):
        pass
    
    @route.patch("/{sensor_id}")
    def partial_update(self, sensor_id : str, 
                       sensor_request : SensorRequestSchema):
        pass
    
    @route.delete("/{sensor_id}")
    def destroy(self, sensor_id : str):
        pass
    
