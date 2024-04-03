from ninja_extra import route, api_controller, ControllerBase
from api.v1.schemas import SensorRequestSchema, SensorResponseSchema, ErrorResponseSchema
from api.v1.services.sensor_service import SensorService
from api.v1.exceptions import BadRequestException, ServerErrorException, NotFoundException


@api_controller("/sensor")
class SensorController(ControllerBase):
    
    @route.post("/{sensor_id}", response={
        201 : SensorResponseSchema, 
        400 : ErrorResponseSchema,
        500 : ErrorResponseSchema
    })
    def create(self, sensor_id : str, sensor_request : SensorRequestSchema):
        try:
            response=SensorService.create(sensor_id, sensor_request)
            return 201, response
        except BadRequestException as e:
            return 400, ErrorResponseSchema(
                status=e.status, 
                detail=e.detail
            )
        except ServerErrorException as e:
            return 500, ErrorResponseSchema(
                status=e.status, 
                detail=e.detail
            )
            
    
    @route.get("/{sensor_id}", response={
        200 : SensorResponseSchema,
        400 : ErrorResponseSchema,
        404 : ErrorResponseSchema,
        500 : ErrorResponseSchema
    })
    def retrieve(self, sensor_id : str):
        try:
            response=SensorService.retrieve(sensor_id)
            return 200, response
        except BadRequestException as e:
            return 400, ErrorResponseSchema(
                status=e.status,
                detail=e.detail
            )
        except NotFoundException as e:
            return 404, ErrorResponseSchema(
                status=e.status,
                detail=e.detail
            )
        except Exception as e:
            return 500, ErrorResponseSchema(
                status=500,
                detail="Internal Server Error"
            )
            
    
    @route.put("/{sensor_id}", response={
        200 : SensorResponseSchema,
        400 : ErrorResponseSchema,
        404 : ErrorResponseSchema,
        500 : ErrorResponseSchema
    })        
    def update(self, sensor_id : str, 
               sensor_request : SensorRequestSchema):
        try:
            response=SensorService.update(sensor_id, sensor_request)
            return 200, response
        except BadRequestException as e:
            return 400, ErrorResponseSchema(
                status=e.status,
                detail=e.detail
            )
        except NotFoundException as e:
            return 404, ErrorResponseSchema(
                status=e.status,
                detail=e.detail
            )
        except Exception as e:
            return 500, ErrorResponseSchema(
                status=500,
                detail="Internal Server Error"
            )

    
    @route.delete("/{sensor_id}", response={
        204 : dict,
        404 : ErrorResponseSchema,
        500 : ErrorResponseSchema
    })
    def destroy(self, sensor_id : str):
        try:
            if SensorService.destroy(sensor_id):
                return 204, {"detail" : "Successfully Remove Collection"}
        except NotFoundException as e:
            return 404, ErrorResponseSchema(
                status=e.status,
                detail=e.detail
            )
        except ServerErrorException as e:
            return 500, ErrorResponseSchema(
                status=e.status, 
                detail=e.detail
            )
