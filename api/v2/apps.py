from django.apps import AppConfig


class V2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api.v2'

    
    def ready(self):
        
        from api.v2.admins import (
            MachineAdmin,
            SensorAdmin,
            UserAdmin
        )