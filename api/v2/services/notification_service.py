from api.v2.repositories import (
    MachineRepository, NotificationRepository)
from api.v2.exceptions import (
    NotFoundException, ServerErrorException, 
    BadRequestException)
from api.v2.schemas import (
    MachineSchema, NotificationSchema,
    CreateNotificationSchema)


class NotificationService:
    
    @staticmethod
    def list(machine_code : str):
        
        if not MachineRepository.is_machine_exist(machine_code):
            raise NotFoundException(
                detail = "Machine instance does not exists.")
        
        notifications = NotificationRepository.get_notifications(
            machine_code)
        
        response = [NotificationSchema(**notification.__dict__).dict()
                    for notification in notifications]
    
        return response
    
    
    @staticmethod
    def retrieve(machine_code : str, notification_id : int):
        
        if not MachineRepository.is_machine_exist(machine_code):
            raise NotFoundException(
                detail = "Machine instance does not exists.")
        
        notification = NotificationRepository.get_notification(
            machine_code, notification_id)
        
        if not notification:
            raise NotFoundException(
                detail = "Notification instance does not exists.")
        
        return NotificationSchema(**notification.__dict__).dict()
        
    
    @staticmethod
    def create(machine_code : str, 
               notification_request : CreateNotificationSchema):

        if not MachineRepository.is_machine_exist(machine_code):
            raise NotFoundException(
                detail = "Machine instance does not exists.")

        if not NotificationRepository.create_notification(
            machine_code, notification_request): 
            raise BadRequestException()
        
        return NotificationSchema(**notification_request.dict())