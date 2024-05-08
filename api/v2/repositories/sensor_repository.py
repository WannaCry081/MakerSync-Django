from api.v2.models import (
    Sensor, Machine)


class SensorRepository:
    
    @staticmethod
    def get_sensor(code : str):
        
        machine = Machine.objects.get(code = code)
        sensor = Sensor.objects.filter(
            machine = machine).first()
        
        return sensor
    
    
    @staticmethod 
    def create_sensor(code : str):
        
        machine = Machine.objects.get(code = code)
        sensor = Sensor.objects.create(
            machine = machine)
        
        if sensor:
            return True
        
        return False