from ninja_extra import (
    route, api_controller, ControllerBase)
from api.v1.schemas import (
    ErrorSchema, CreateSensorSchema, SensorSchema)
from api.v1.exceptions import (
    BadRequestException, ServerErrorException, 
    NotFoundException)
from api.v1.services.sensor_service import SensorService


@api_controller("/sensors")
class SensorController(ControllerBase):
    """
    Controller handling operations related to sensors.
    """

    @route.post("/", 
                summary = "Create a new sensor", 
                description = "Create a new sensor with the provided ID.",
                response={
                    201 : SensorSchema, 
                    400 : ErrorSchema,
                    500 : ErrorSchema
                })
    def create(self, sensor_request : CreateSensorSchema):
        """
        Endpoint to create a new sensor.
        
        Args:
            sensor_request (CreateSensorSchema): The request data for adding the record of the machine in the database.

        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            response = SensorService.create(sensor_request)
            return 201, response
        except BadRequestException as e:
            return 400, ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return 500, ErrorSchema(**e.__dict__)
            
    
    @route.get("/{sensor_id}",
               summary = "Retrieve a sensor",
               description = "Retrieve details of a sensor with the provided ID.", 
               response = {
                    200 : SensorSchema,
                    400 : ErrorSchema,
                    404 : ErrorSchema,
                    500 : ErrorSchema
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
            return 400, ErrorSchema(**e.__dict__)
        except NotFoundException as e:
            return 404, ErrorSchema(**e.__dict__)
        except Exception as e:
            return 500, ErrorSchema(
                status = 500,
                detail = "Internal Server Error"
            )
            
    
    @route.put("/{sensor_id}", 
               summary = "Update a sensor",
               description = "Update details of a sensor with the provided ID.",
               response = {
                200 : SensorSchema,
                400 : ErrorSchema,
                404 : ErrorSchema,
                500 : ErrorSchema
                })        
    def update(self, sensor_id : str, 
               sensor_request : SensorSchema):
        """
        Endpoint to update details of a sensor.
        
        Args:
            sensor_id (str): The ID of the sensor to update.
            sensor_request (SensorSchema): The request data for updating the sensor.
        
        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            response = SensorService.update(sensor_id, sensor_request)
            return 200, response
        except BadRequestException as e:
            return 400, ErrorSchema(**e.__dict__)
        except NotFoundException as e:
            return 404, ErrorSchema(**e.__dict__)
        except Exception as e:
            return 500, ErrorSchema(
                status = 500,
                detail = "Internal Server Error"
            )

    
    @route.delete("/{sensor_id}", 
                  summary = "Delete a sensor",
                  description = "Delete a sensor with the provided ID.",
                  response={
                    204 : dict,
                    404 : ErrorSchema,
                    500 : ErrorSchema
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
            return 404, ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return 500, ErrorSchema(**e.__dict__)