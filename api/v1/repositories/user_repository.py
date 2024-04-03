from api.v1.schemas import UserRequestSchema
from api.v1.utils import firebase_firestore
from typing import List 

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
       return True  
   
    @staticmethod
    def is_user_exists(sensor_id: str, email : str):
        user_doc=db.collection(sensor_id).document(email).get()
        return user_doc.exists
        
    @staticmethod
    def get_user(sensor_id: str, email: str):
        user=db.collection(sensor_id).document(email).get()
        if user.exists:
            return user.to_dict()
        return None
    
    @staticmethod
    def get_users(sensor_id: str):
        users=[]

        try:
            docs=db.collection(sensor_id).stream()
            for doc in docs:
                if doc.id != "sensors":
                    users.append(doc.to_dict())
        
        except Exception as e:
            print("Error:", e)

        return users
    
    @staticmethod
    def update_user(sensor_id: str, email: str, user_request: UserRequestSchema):
        user=db.collection(sensor_id).document(email)
        user.update(user_request.dict())
        return True
    
    @staticmethod 
    def delete_user(sensor_id: str, email):
        user=db.collection(sensor_id).document(email)
        user.delete()
        return True
    
    