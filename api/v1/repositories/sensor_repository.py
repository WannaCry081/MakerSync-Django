from api.v1.schemas import SensorSchema
from api.v1.utils import firebase_firestore


db = firebase_firestore()


class SensorRepository:
    
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