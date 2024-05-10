from typing import List
from ninja_extra import (
    api_controller, ControllerBase, route)
from api.v2.schemas import (
    NotificationSchema, CreateNotificationSchema,
    ErrorSchema)
from api.v2.exceptions import (
    NotFoundException, ServerErrorException,
    BadRequestException)
from api.v2.services import NotificationService


@api_controller("/machines/{machine_code}/notifications")
class NotificationController(ControllerBase):
    """
    Controller for handling notifications.
    """
    
    @route.get("/",
               summary = "Retrieves a list of notification instance.",
               description = "Retrieves a list of notification instance based on the path parameter inputted.",
               response = {
                   200 : List[NotificationSchema],
                   404 : ErrorSchema,
                   500 : ErrorSchema
               })
    def list(self, machine_code : str):
        """
        Endpoint to retrieve a list of notifications of a given machine.

        Args:
            machine_code (str): The ID of the machine.

        Returns:
            tuple: A tuple containing status code and response data.
        """
        try: 
            response = NotificationService.list(machine_code)
            return 200, response
        except NotFoundException as e:
            return 404, ErrorSchema(**e.__dict__)
        except:
            return 500, ErrorSchema(
                **ServerErrorException().__dict__)
    
    
    @route.get("/{notification_id}")
    def retrieve(self, machine_code : str, notification_id : int):
        try:
            response = NotificationService.retrieve(
                machine_code, notification_id)
            return response
        except NotFoundException as e:
            return ErrorSchema(**e.__dict__)
        except:
            return ErrorSchema(
                **ServerErrorException().__dict__)

    
    @route.post("/")
    def create(self, machine_code : str, 
               notification_request : CreateNotificationSchema):
        try:
            response = NotificationService.create(
                machine_code, notification_request)
            return response
        except BadRequestException as e:
            return ErrorSchema(**e.__dict__)
        except NotFoundException as e:
            return ErrorSchema(**e.__dict__)
        except:
            return ServerErrorException(
                **ServerErrorException().__dict__)