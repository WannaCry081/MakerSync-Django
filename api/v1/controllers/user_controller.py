from ninja_extra import ControllerBase, api_controller, route


@api_controller("/users")
class UserController(ControllerBase):
    
    @route.get("/{sensor_id}")
    def list(self, sensor_id : str):
        pass
    
    
    @route.post("/{sensor_id}")
    def create(self, sensor_id : str):
        pass 
    
    
    @route.get("/{sensor_id}/{user_email}")
    def retrieve(self, sensor_id : str, user_email : str):
        pass
    
    
   