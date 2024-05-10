from api.v1.schemas import SensorSchema
from api.v1.utils import firebase_firestore


db = firebase_firestore()


class MachineRepository:
    
    @staticmethod
    def create_sensor(code : str):
        doc = db.collection(code).document("sensors")
        doc.set(SensorSchema().dict())
        return True
    
    
    @staticmethod
    def is_sensor_exists(code : str):
        collection = db.collection(code).get()
        return len(collection) == 0
    
    
    @staticmethod
    def get_sensor(code : str):
        sensor = db.collection(code).document("sensors").get()
        
        if sensor.exists:
            return sensor.to_dict()
        
        return None
    
    
    @staticmethod
    def update_sensor(code : str, **kwargs):
        sensor = db.collection(code).document("sensors")
        sensor.update(kwargs)
        return True
    
    
    @staticmethod
    def delete_sensor(code : str):
        collection = db.collection(code)
        
        for document in collection.stream():
            document.reference.delete()
    
        return True 