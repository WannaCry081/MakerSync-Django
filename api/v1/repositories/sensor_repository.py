from firebase_admin import firestore


db=firestore.client()


class SensorRepository:
    
    @staticmethod
    def create_sensor(sensor_id : str, sensor_request : SensorRequestSchema):
        pass