from django.db.models import Q
from api.v2.schemas import (
    MachineSchema, CreateNotificationSchema)
from api.v2.models import (
    Notification, Machine)


class NotificationRepository:
    
    @staticmethod
    def get_notifications(code : str):
        machine = Machine.objects.get(code = code)
        notifications = Notification.objects.filter(
            machine = machine)

        return notifications
    
    
    @staticmethod
    def get_notification(code : str, notification_id : int):
        machine = Machine.objects.get(code = code)
        notification = Notification.objects.filter(
            Q(machine = machine) & Q(id = notification_id)).first()
        
        return notification
    
    
    @staticmethod
    def create_notification(code : str, 
                            notification_request : CreateNotificationSchema):
        machine = Machine.objects.get(code = code)
        notification = Notification.objects.create(
            **notification_request.dict(), machine = machine)
        
        if notification:
            return True
        
        return False