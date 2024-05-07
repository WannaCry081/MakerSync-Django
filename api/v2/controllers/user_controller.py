from ninja_extra import (
    api_controller, ControllerBase, route)
from api.v2.schemas import (
    MachineSchema, UserSchema)


@api_controller("/machines/{machine_id}/users")
class UserController(ControllerBase):
    
    @route.get("/")
    def list(self, machine_id : MachineSchema):
        pass
    
    
    @route.get("/{email}")
    def retrieve(self, machine_id : MachineSchema, email : str):
        pass
    
    
    @route.post("/")
    def create(self, machine_id : MachineSchema, 
               request : UserSchema):
        pass
    
    
    @route.put("/{email}")
    def update(self, machine_id : MachineSchema, 
               email : str, request : UserSchema):
        pass
    
    
    @route.delete("/{email}")
    def destroy(self, machine_id : MachineSchema, email : str):
        pass