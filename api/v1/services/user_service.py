from pydantic import EmailStr
from typing import List
from api.v1.schemas import UserSchema
from api.v1.repositories import (
    UserRepository, MachineRepository)
from api.v1.exceptions import (
    BadRequestException, NotFoundException, 
    ServerErrorException, ConflictException)


class UserService:
    
    @staticmethod    
    def list(machine_code : str):
        
        if not MachineRepository.is_machine_exists(machine_code):
            raise NotFoundException(
                detail = "Machine instance does not exists.")

        return UserRepository.get_users(machine_code)
     
    
    
    @staticmethod    
    def create(machine_code : str, user_request: UserSchema):
        
        if not MachineRepository.is_machine_exists(machine_code):
            raise NotFoundException(
                detail="Machine instance does not exists.")
            
        email : EmailStr = user_request.email
        if UserRepository.is_user_exists(machine_code, email):
            raise ConflictException(
                detail="Duplicate user instance.")
        
        if not UserRepository.create_user(
            machine_code, **user_request.dict()):
            raise BadRequestException()
        
        return user_request
    
    
    @staticmethod    
    def retrieve(machine_code : str, email : EmailStr):
        
        if not MachineRepository.is_machine_exists(machine_code):
            raise NotFoundException(
                detail = "Machine instance does not exists.")
        
        if not UserRepository.is_user_exists(machine_code, email):
            raise NotFoundException(
                detail="User does not exists.")
        
        user = UserRepository.get_user(machine_code, email)
        if not user:
            raise BadRequestException()
        
        return UserSchema(**user)

    
    @staticmethod    
    def update(machine_code : str, email: EmailStr, user_request : UserSchema):
        
        if not MachineRepository.is_machine_exists(machine_code):
            raise NotFoundException(
                detail = "Machine instance does not exists.")
            
        if not UserRepository.get_user(machine_code, email):
            raise NotFoundException(
                detail="User does not exists.")
        
        user = UserRepository.update_user(
            machine_code, **user_request.dict())
        if not user:
            raise BadRequestException()
        
        return user_request
    
    
    @staticmethod    
    def destroy(machine_code : str, email : EmailStr):
        
        if not MachineRepository.is_machine_exists(machine_code):
            raise NotFoundException(
                detail = "Machine instance does not exists.")
            
        if not UserRepository.get_user(machine_code, email):
            raise NotFoundException(
                detail="User does not exists.")
        
        if not UserRepository.delete_user(machine_code, email):
            raise BadRequestException()
        
        return True