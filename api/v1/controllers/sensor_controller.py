from ninja_extra import route, api_controller, ControllerBase


@api_controller("/sensor")
class SensorController(ControllerBase):
    
    @route.post("/")
    def create(self):
        pass
    
    