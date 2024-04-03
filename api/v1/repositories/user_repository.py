from api.v1.schemas import UserRequestSchema
from api.v1.utils import firebase_firestore


db=firebase_firestore()


class UserRepository:
    
    @staticmethod
    def create_user(sensor_id: str, user_request: UserRequestSchema):
       pass
   
    @staticmethod
    def is_user_exists(sensor_id: str):
        pass
    
    @staticmethod
    def get_user(sensor_id: str):
        pass
    
    
    