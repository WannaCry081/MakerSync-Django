from ninja_extra import (
    api_controller, ControllerBase, route)
from api.v2.schemas import (
    MachineSchema, SensorSchema)
from api.v2.services import (
    SensorService)
from api.v2.exceptions import (
    ConflictException, ServerErrorException,
    NotFoundException, BadRequestException)
from api.v2.schemas import ErrorSchema


@api_controller("/machines/{machine_code}/sensors")
class SensorController(ControllerBase):
    """
    Controller handling the Sensor instance.
    """
    
    @route.get("",
               summary = "Retrieves a sensor instance.",
               description = "Retrieves a sensor instance based on the path parameter inputted",
               response = {
                   200 : SensorSchema,
                   404 : ErrorSchema,
                   500 : ErrorSchema
               })
    def retrieve(self, machine_code : str):
        """
        Endpoint to retrieves a sensor instance based on the machine code.

        Args:
            machine_code (str): The ID of the machine.

        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            response = SensorService.retrieve(machine_code)
            return 200, response
        except NotFoundException as e:
            return 404, ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return 500, ErrorSchema(**e.__dict__)
            
    
    @route.post("", 
                summary = "Create a new sensor instance.", 
                description = "Creates a new sensor instance based on the path parameter inputted.", 
                response = {
                    201 : SensorSchema,
                    404 : ErrorSchema, 
                    409 : ErrorSchema,
                    500 : ErrorSchema
                })
    def create(self, machine_code : str):
        """
        Endpoint to create a new sensor instance based on the machine code.

        Args:
            machine_code (str): The ID of the machine.

        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            response = SensorService.create(machine_code)
            return 201, response
        except NotFoundException as e:
            return 404, ErrorSchema(**e.__dict__)
        except ConflictException as e:
            return 409, ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return 500, ErrorSchema(**e.__dict__)
    
    
    @route.put("", 
               summary = "Updates the sensor data.",
               description = "Updates the sensor data based on the request data and machine code.", 
               response = {
                   200 : SensorSchema,
                   400 : ErrorSchema, 
                   404 : ErrorSchema,
                   500 : ErrorSchema
               })
    def update(self, machine_code : str, 
               sensor_request : SensorSchema):
        """
        Endpoint to update the data of the sensor instance based on the request dat and machine code.

        Args:
            machine_code (str): The ID of the machine.
            sensor_request (SensorSchema): The request data for updating the sensor instance.

        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            response = SensorService.update(
                machine_code, sensor_request)
            return 200, response
        except BadRequestException as e:
            return 400, ErrorSchema(**e.__dict__)
        except NotFoundException as e:
            return 404, ErrorSchema(**e.__dict__)
        except:
            return 500, ErrorSchema(
                **ServerErrorException().__dict__)
    
    
    @route.delete("", 
                  summary = "Deletes the sensor instance.",
                  description = "Deletes the sensor instance based on the path parameter inputted.", 
                  response = {
                      204 : dict, 
                      404 : ErrorSchema,
                      500 : ErrorSchema
                  })
    def destroy(self, machine_code : str):
        """
        Endpoint to remove a sensor instance based on the machine code.

        Args:
            machine_code (str): The ID of the machine.

        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            response = SensorService.destroy(machine_code)
            return 204, response
        except NotFoundException as e:
            return 404, ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return 500, ErrorSchema(**e.__dict__)