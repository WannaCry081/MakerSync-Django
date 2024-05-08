from api.v1.schemas import SensorRequestSchema
from api.v1.utils import firebase_firestore


db = firebase_firestore()


class SensorRepository:
    
    @staticmethod
    def create_sensor(sensor_id : str):
        doc=db.collection(sensor_id).document("sensors")
        doc.set({
            "is_start" : False,
            "is_stop" : False,
            "is_initialize" : False,
            "counter" : 0,
            "time" : 0,
            "temperature" : 0
        })
        return True
    
    
    @staticmethod
    def is_sensor_exists(sensor_id : str):
        collection=db.collection(sensor_id).get()
        return len(collection) == 0
    
    
    @staticmethod
    def get_sensor(sensor_id : str):
        sensor=db.collection(sensor_id).document("sensors").get()
        if sensor.exists:
            return sensor.to_dict()
        return None
    
    
    @staticmethod
    def update_sensor(sensor_id : str, sensor_request : SensorRequestSchema):
        sensor=db.collection(sensor_id).document("sensors")
        sensor.update(sensor_request.dict())
        return True
    
    
    @staticmethod
    def delete_sensor(sensor_id : str):
        collection=db.collection(sensor_id)
        
        for document in collection.stream():
            document.reference.delete()
    
        return True 