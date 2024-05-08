from api.v2.models import (
    Sensor, Machine)


class SensorRepository:
    
    @staticmethod
    def get_sensor(code : str):
        
        machine = Machine.objects.get(code = code)
        sensor = Sensor.objects.filter(
            machine = machine).first()
        
        return sensor