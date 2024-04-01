from firebase_admin import firestore


db=firestore.client()


class SensorRepository:
    
    @staticmethod
    def create_sensor(sensor_id : str, sensor_request : SensorRequestSchema):
        doc=db.collection(sensor_id).document("sensors")
        doc.set({
            "is_start" : sensor_request.is_start,
            "is_stop" : sensor_request.is_stop,
            "is_initialized" : sensor_request.is_initialized,
            "counter" : sensor_request.counter,
            "timer" : sensor_request.timer
        })
        return True