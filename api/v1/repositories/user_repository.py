from api.v1.schemas import UserSchema
from api.v1.utils import firebase_firestore
from typing import List 

db = firebase_firestore()


class UserRepository:
    
    @staticmethod
    def create_user(code: str, **kwargs):
        if not ("email" in kwargs and "username" in kwargs):
            return False
        
        doc = db.collection(code).document(kwargs["email"])
        doc.set(kwargs)
        return True  
   
   
    @staticmethod
    def is_user_exists(code: str, email : str):
        user_doc = db.collection(code).document(email).get()
        return user_doc.exists


    @staticmethod
    def get_user(code: str, email: str):
        user = db.collection(code).document(email).get()
        if user.exists:
            return user.to_dict()
        return None


    @staticmethod
    def get_users(code: str):
        users = []

        docs = db.collection(code).stream()
        users = [doc.to_dict() for doc in docs if doc.id != "sensors"]
        return users


    @staticmethod
    def update_user(code: str, **kwargs):
        
        if not ("email" in kwargs and "username" in kwargs):
            return False
        
        user = db.collection(code).document(kwargs["email"])
        user.update(kwargs)
        return True


    @staticmethod 
    def delete_user(code: str, email : str):
        user = db.collection(code).document(email)
        user.delete()
        return True