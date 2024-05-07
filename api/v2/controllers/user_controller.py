from pydantic import EmailStr
from ninja_extra import (
    api_controller, ControllerBase, route)
from api.v2.schemas import (
    MachineSchema, UserSchema)


@api_controller("/machines/{machine_code}/users")
class UserController(ControllerBase):
    
    @route.get("/")
    def list(self, machine_code : str):
        pass
    
    
    @route.get("/{email}")
    def retrieve(self, machine_code : str, email : EmailStr):
        pass
    
    
    @route.post("/")
    def create(self, machine_code : str, 
               request : UserSchema):
        pass
    
    
    @route.put("/{email}")
    def update(self, machine_code : str, 
               email : EmailStr, request : UserSchema):
        pass
    
    
    @route.delete("/{email}")
    def destroy(self, machine_code : str, email : EmailStr):
        pass