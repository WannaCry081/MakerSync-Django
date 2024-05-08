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
    
    
    @staticmethod
    def update_sensor(code : str, **kwargs):
        
        sensor_values = [
            "is_start",
            "is_stop",
            "is_initialize",
            "temperature",
            "time",
            "counter"
        ]
        
        if not all(key in sensor_values for key in kwargs.keys()):
            return False
        
        machine = Machine.objects.get(code = code)
        sensor = Sensor.objects.get(machine = machine)
        
        for key, value in kwargs.items():
            setattr(sensor, key, value)
            
        sensor.save()
        return True