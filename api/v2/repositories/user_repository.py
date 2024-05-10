from pydantic import EmailStr
from django.db.models import Q
from api.v2.models import ( 
    Machine, User)


class UserRepository:
    
    @staticmethod 
    def is_user_exist(code : str, email : EmailStr):
        
        machine = Machine.objects.get(code = code)
        user = User.objects.filter(
            Q(machine = machine) & Q(email = email)
        ).first()
        
        if user:
            return True
        
        return False
        
    
    @staticmethod 
    def get_users(code : str):
        
        machine = Machine.objects.get(code = code)
        users = User.objects.filter(
            machine = machine).all()
        
        return users
    
    
    @staticmethod 
    def get_user(code : str, email : EmailStr):
        
        machine = Machine.objects.get(code = code)
        user = User.objects.filter(
            Q(machine = machine) & Q(email = email)
        ).first()
        
        return user
    
    
    @staticmethod
    def create_user(code : str, **kwargs):
        
        if not ("username" in kwargs and "email" in kwargs):
            return False
        
        machine = Machine.objects.get(code = code)
        user = User.objects.create(
            **kwargs, machine = machine)
        
        if user:
            return True
        
        return False
    
    
    @staticmethod
    def update_user(code : str, user, **kwargs):
        
        if not ("username" in kwargs and "email" in kwargs):
            return False
        
        for key, value in kwargs.items():
            setattr(user, key, value)
        
        user.save()
        return True
    
    
    @staticmethod
    def delete_user(user):
        user.delete()
        return True