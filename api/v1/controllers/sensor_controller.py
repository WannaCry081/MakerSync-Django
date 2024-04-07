from ninja_extra import route, api_controller, ControllerBase
from api.v1.schemas import SensorRequestSchema, SensorResponseSchema, ErrorResponseSchema
from api.v1.services.sensor_service import SensorService
from api.v1.exceptions import BadRequestException, ServerErrorException, NotFoundException


@api_controller("/sensors")
class SensorController(ControllerBase):
    """
    Controller handling operations related to sensors.
    """
    
    @route.get("/")
    def list(self):
        try:
            pass    
        except:
            pass
        

    @route.post("/{sensor_id}", 
                summary = "Create a new sensor", 
                description = "Create a new sensor with the provided ID.",
                response={
                    201 : SensorResponseSchema, 
                    400 : ErrorResponseSchema,
                    500 : ErrorResponseSchema
                })
    def create(self, sensor_id : str):
        """
        Endpoint to create a new sensor.
        
        Args:
            sensor_id (str): The ID of the sensor.

        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            response = SensorService.create(sensor_id)
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
            
    
    @route.get("/{sensor_id}",
               summary = "Retrieve a sensor",
               description = "Retrieve details of a sensor with the provided ID.", 
               response = {
                    200 : SensorResponseSchema,
                    400 : ErrorResponseSchema,
                    404 : ErrorResponseSchema,
                    500 : ErrorResponseSchema
                })
    def retrieve(self, sensor_id : str):
        """
        Endpoint to retrieve details of a sensor.
        
        Args:
            sensor_id (str): The ID of the sensor to retrieve.
        
        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            response = SensorService.retrieve(sensor_id)
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
            
    
    @route.put("/{sensor_id}", 
               summary = "Update a sensor",
               description = "Update details of a sensor with the provided ID.",
               response = {
                200 : SensorResponseSchema,
                400 : ErrorResponseSchema,
                404 : ErrorResponseSchema,
                500 : ErrorResponseSchema
                })        
    def update(self, sensor_id : str, 
               sensor_request : SensorRequestSchema):
        """
        Endpoint to update details of a sensor.
        
        Args:
            sensor_id (str): The ID of the sensor to update.
            sensor_request (SensorRequestSchema): The request data for updating the sensor.
        
        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            response = SensorService.update(sensor_id, sensor_request)
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

    
    @route.delete("/{sensor_id}", 
                  summary = "Delete a sensor",
                  description = "Delete a sensor with the provided ID.",
                  response={
                    204 : dict,
                    404 : ErrorResponseSchema,
                    500 : ErrorResponseSchema
                    })
    def destroy(self, sensor_id : str):
        """
        Endpoint to delete a sensor.
        
        Args:
            sensor_id (str): The ID of the sensor to delete.
        
        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            if SensorService.destroy(sensor_id):
                return 204, {"detail" : "Successfully delete collection"}
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
