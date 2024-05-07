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
        
        return NotificationRepository.get_notifications(machine_code)
    
    
    @staticmethod
    def retrieve(machine_id : MachineSchema, notification_id : int):
        pass
    
    
    @staticmethod
    def create(machine_id : MachineSchema, request : NotificationSchema):
        pass