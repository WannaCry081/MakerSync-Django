from ninja_extra import ControllerBase, api_controller, route


@api_controller("/users")
class UserController(ControllerBase):
    
    @route.get("/{sensor_id}")
    def list(self, sensor_id : str):
        pass
    