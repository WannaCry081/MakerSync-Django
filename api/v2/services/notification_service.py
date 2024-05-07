from api.v2.repositories import (
    MachineRepository, NotificationRepository)
from api.v2.exceptions import (
    NotFoundException, ServerErrorException)
from api.v2.schemas import (
    MachineSchema, NotificationSchema)


class NotificationService:
    
    @staticmethod
    def list(machine_code : str):
        
        if not MachineRepository.is_machine_exist(machine_code):
            raise NotFoundException()
        
        notifications = NotificationRepository.get_notifications(
            machine_code)
        
        response = [NotificationSchema(**notification.__dict__).dict()
                    for notification in notifications]
    
        return response
        
    
    
    @staticmethod
    def retrieve(machine_code : str, notification_id : int):
        
        if not MachineRepository.is_machine_exist(machine_code):
            raise NotFoundException()
        
        notification = NotificationRepository.get_notification(
            machine_code, notification_id)
        
        if not notification:
            raise NotFoundException()
        
        return NotificationSchema(**notification.__dict__).dict()
        
    
    @staticmethod
    def create(machine_id : MachineSchema, request : NotificationSchema):
        pass