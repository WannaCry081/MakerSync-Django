from ninja_extra import ControllerBase, api_controller, route


@api_controller("/users")
class UserController(ControllerBase):
    
    @route.get("/{sensor_id}")
    def list(self, sensor_id : str):
        pass
    
    
    @route.post("/{sensor_id}")
    def create(self, sensor_id : str):
        pass 
    
    
    