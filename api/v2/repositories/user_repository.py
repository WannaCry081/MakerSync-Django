from api.v2.models import (
    Machine, User)


class UserRepository:
    
    @staticmethod 
    def get_users(code : str):
        
        machine = Machine.objects.get(code = code)
        users = User.objects.filter(
            machine = machine).all()
        
        return users