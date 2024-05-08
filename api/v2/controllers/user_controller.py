from pydantic import EmailStr
from ninja_extra import (
    api_controller, ControllerBase, route)
from api.v2.schemas import (
    MachineSchema, UserSchema, ErrorSchema)
from api.v2.exceptions import (
    NotFoundException, ServerErrorException,
    BadRequestException, ConflictException)
from api.v2.services import UserService


@api_controller("/machines/{machine_code}/users")
class UserController(ControllerBase):
    
    @route.get("/")
    def list(self, machine_code : str):
        try:
            response = UserService.list(machine_code)
            return response
        except NotFoundException as e:
            return ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return ErrorSchema(**e.__dict__)
    
    
    @route.get("/{email}")
    def retrieve(self, machine_code : str, email : EmailStr):
        try:
            response = UserService.retrieve(
                machine_code, email)
            return response
        except NotFoundException as e:
            return ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return ErrorSchema(**e.__dict__)
    
    
    @route.post("/")
    def create(self, machine_code : str, 
               user_request : UserSchema):
        try:
            response = UserService.create(
                machine_code, user_request)
            return response
        except BadRequestException as e:
            return ErrorSchema(**e.__dict__)
        except NotFoundException as e:
            return ErrorSchema(**e.__dict__)
        except ConflictException as e:
            return ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return ErrorSchema(**e.__dict__)
        
        
    @route.put("/{email}")
    def update(self, machine_code : str, 
               email : EmailStr, user_request : UserSchema):
        try:
            response = UserService.update(
                machine_code, email, user_request)
            return response
        except BadRequestException as e:
            return ErrorSchema(**e.__dict__)
        except NotFoundException as e:
            return ErrorSchema(**e.__dict__)
        except ConflictException as e:
            return ErrorSchema(**e.__dict__)
        except ServerErrorException as e:
            return ErrorSchema(**e.__dict__)
        
    
    @route.delete("/{email}")
    def destroy(self, machine_code : str, email : EmailStr):
        pass