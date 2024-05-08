from pydantic import EmailStr
from api.v2.repositories import (
    MachineRepository, UserRepository)
from api.v2.exceptions import  (
    NotFoundException, ServerErrorException, 
    BadRequestException, ConflictException)
from api.v2.schemas import (
    UserSchema)

class UserService:
    
    @staticmethod
    def list(machine_code : str):
        
        if not MachineRepository.is_machine_exist(
            machine_code):
            raise NotFoundException()
        
        users = UserRepository.get_users(machine_code)
        
        if not users:
            return []
        
        response = [UserSchema(**user.__dict__).dict() 
                    for user in users]
        
        return response
        
        
    @staticmethod
    def retrieve(machine_code : str, email : EmailStr):
        
        if not MachineRepository.is_machine_exist(
            machine_code):
            raise NotFoundException()
        
        if not UserRepository.is_user_exist(
            machine_code, email):
            raise NotFoundException()
        
        user = UserRepository.get_user(
            machine_code, email)
        
        return UserSchema(**user.__dict__).dict()
    
    
    @staticmethod
    def create(machine_code : str, user_request : UserSchema):
        
        if not MachineRepository.is_machine_exist(
            machine_code):
            raise NotFoundException()
        
        if UserRepository.is_user_exist(
            machine_code, user_request.email):
            raise ConflictException()

        user = UserRepository.create_user(
            machine_code, **user_request.dict())
        
        if not user:
            return BadRequestException()

        return user_request.dict()
        
        