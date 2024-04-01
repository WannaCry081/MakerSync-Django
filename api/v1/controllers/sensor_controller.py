from ninja_extra import route, api_controller, ControllerBase


@api_controller("/sensor")
class SensorController(ControllerBase):
    
    @route.post("/")
    def create(self):
        pass
    
    @route.get("/{sensor_id}")
    def retrieve(self, sensor_id : str):
        pass
    
    @route.put("/{sensor_id}")        
    def update(self, sensor_id : str):
        pass
    