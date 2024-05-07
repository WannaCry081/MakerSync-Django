from api.v2.schemas import (
    MachineSchema, NotificationSchema)
from api.v2.models import (
    Notification, Machine)


class NotificationRepository:
    
    @staticmethod
    def get_notifications(code : str):
        machine = Machine.objects.get(code = code)
        notifications = Notification.objects.filter(
            machine = machine)

        return [NotificationSchema(
            **notification.__dict__).dict() 
            for notification in notifications]