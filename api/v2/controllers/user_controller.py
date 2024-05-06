from ninja_extra import (
    api_controller, ControllerBase, route)
from api.v2.schemas import (
    MachineSchema, UserSchema)


@api_controller("/machines/{code}/users")
class UserController(ControllerBase):
    
    @route.get("/")
    def list(self, code : MachineSchema):
        pass
    
    
    @route.get("/{email}")
    def retrieve(self, code : MachineSchema, email : str):
        pass
    
    
    @route.post("/")
    def create(self, code : MachineSchema, 
               request : UserSchema):
        pass
    
    
    @route.put("/{email}")
    def update(self, code : MachineSchema, 
               email : str, request : UserSchema):
        pass