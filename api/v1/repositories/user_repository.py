from api.v1.schemas import UserRequestSchema
from api.v1.utils import firebase_firestore


db=firebase_firestore()


class UserRepository:
    
    @staticmethod
    def create_user(sensor_id: str, user_request: UserRequestSchema):
       doc=db.collection(sensor_id).document(user_request.email)
       doc.set({
           "name" : user_request.name,
           "email" : user_request.email,
           "is_active" : user_request.is_active,
           "is_connected" : user_request.is_connected
       })
   
    @staticmethod
    def is_user_exists(sensor_id: str, user_request: UserRequestSchema):
        user_doc=db.collection(sensor_id).document(user_request.email).get()
        return user_doc.exists
        
    @staticmethod
    def get_user(sensor_id: str):
        pass
    
    @staticmethod
    def get_users(sensor_id: str):
        pass
    
    @staticmethod
    def update_user(sensor_id: str, user_request: UserRequestSchema):
        pass
    
    @staticmethod 
    def delete_user(sensor_id: str):
        pass
    
    