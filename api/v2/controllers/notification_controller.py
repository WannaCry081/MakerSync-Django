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
    
    @route.get("",
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
    
    
    @route.get("/{notification_id}", 
               summary = "Retrieves a notification instance.",
               description = "Retrieves a specific notification instance based on the path parameter inputted.", 
               response = {
                   200 : NotificationSchema, 
                   404 : ErrorSchema, 
                   500 : ErrorSchema
               })
    def retrieve(self, machine_code : str, notification_id : int):
        """
        Endpoint to retrieve a notification instance based on the machine code and notification ID.

        Args:
            machine_code (str): The ID of the machine.
            notification_id (int): The ID of the notification.

        Returns:
            tuple: A tuple containing status code and response data. 
        """
        try:
            response = NotificationService.retrieve(
                machine_code, notification_id)
            return 200, response
        except NotFoundException as e:
            return 404, ErrorSchema(**e.__dict__)
        except:
            return 500, ErrorSchema(
                **ServerErrorException().__dict__)

    
    @route.post("", 
                summary = "Creates a new notification instance.",
                description = "Creates a new notification instance based on the path parameter inputted.",
                response = {
                    201 : NotificationSchema,
                    400 : ErrorSchema,
                    404 : ErrorSchema,
                    500 : ErrorSchema
                })
    def create(self, machine_code : str, 
               notification_request : CreateNotificationSchema):
        """
        Endpoint to create a new notification instance based on the machine code.

        Args:
            machine_code (str): The ID of the machine.
            notification_request (CreateNotificationSchema): The request data for creating a new notification instance.

        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            response = NotificationService.create(
                machine_code, notification_request)
            return 201, response
        except BadRequestException as e:
            return 400, ErrorSchema(**e.__dict__)
        except NotFoundException as e:
            return 404, ErrorSchema(**e.__dict__)
        except:
            return 500, ErrorSchema(
                **ServerErrorException().__dict__)