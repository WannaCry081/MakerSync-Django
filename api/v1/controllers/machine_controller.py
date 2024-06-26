from ninja_extra import (
    route, api_controller, ControllerBase)
from api.v1.schemas import (
    ErrorSchema, CreateSensorSchema, SensorSchema)
from api.v1.exceptions import (
    BadRequestException, ServerErrorException, 
    NotFoundException, ConflictException)
from api.v1.services import MachineService


@api_controller("/machines")
class MachineController(ControllerBase):
    """
    Controller handling operations related to sensors.
    """

    @route.post("/", 
                summary = "Create a new machine", 
                description = "Create a new sensor instance with the provided ID.",
                response={
                    201 : SensorSchema, 
                    400 : ErrorSchema,
                    409 : ErrorSchema,
                    500 : ErrorSchema
                })
    def create(self, sensor_request : CreateSensorSchema):
        """
        Endpoint to create a machine instance and return a sensor instance.
        
        Args:
            sensor_request (CreateSensorSchema): The request data for adding the record of the machine in the database.

        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            response = MachineService.create(sensor_request)
            return 201, response
        except BadRequestException as e:
            return 400, ErrorSchema(**e.__dict__)
        except ConflictException as e:
            return 409, ErrorSchema(**e.__dict__)
        except:
            return 500, ErrorSchema(
                **ServerErrorException().__dict__)
            
    
    @route.get("/{machine_code}/sensors",
               summary = "Retrieve a sensor",
               description = "Retrieve details of a sensor with the provided ID.", 
               response = {
                    200 : SensorSchema,
                    400 : ErrorSchema,
                    404 : ErrorSchema,
                    500 : ErrorSchema
                })
    def retrieve(self, machine_code : str):
        """
        Endpoint to retrieve details of a sensor.
        
        Args:
            machine_code (str): The ID of the sensor to retrieve.
        
        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            response = MachineService.retrieve(machine_code)
            return 200, response
        except BadRequestException as e:
            return 400, ErrorSchema(**e.__dict__)
        except NotFoundException as e:
            return 404, ErrorSchema(**e.__dict__)
        except:
            return 500, ErrorSchema(
                **ServerErrorException().__dict__)
            
    
    @route.put("/{machine_code}/sensors", 
               summary = "Update a sensor",
               description = "Update details of a sensor with the provided ID.",
               response = {
                    200 : SensorSchema,
                    400 : ErrorSchema,
                    404 : ErrorSchema,
                    500 : ErrorSchema
                })        
    def update(self, machine_code : str, 
               sensor_request : SensorSchema):
        """
        Endpoint to update details of a sensor.
        
        Args:
            machine_code (str): The ID of the sensor to update.
            sensor_request (SensorSchema): The request data for updating the sensor.
        
        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            response = MachineService.update(
                machine_code, sensor_request)
            return 200, response
        except BadRequestException as e:
            return 400, ErrorSchema(**e.__dict__)
        except NotFoundException as e:
            return 404, ErrorSchema(**e.__dict__)
        except:
            return 500, ErrorSchema(
                **ServerErrorException().__dict__)

    
    @route.delete("/{machine_code}/sensors", 
                  summary = "Delete a sensor",
                  description = "Delete a sensor with the provided ID.",
                  response={
                    204 : dict,
                    404 : ErrorSchema,
                    500 : ErrorSchema
                    })
    def destroy(self, machine_code : str):
        """
        Endpoint to delete a sensor.
        
        Args:
            machine_code (str): The ID of the sensor to delete.
        
        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            if MachineService.destroy(machine_code):
                return 204, {}
        except NotFoundException as e:
            return 404, ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return 500, ErrorSchema(**e.__dict__)