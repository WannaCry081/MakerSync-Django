from ninja_extra import route, api_controller, ControllerBase
from api.v1.schemas import SensorRequestSchema, SensorResponseSchema


@api_controller("/sensor")
class SensorController(ControllerBase):
    
    @route.post("/")
    def create(self, sensor_request : SensorRequestSchema):
        pass
    
    @route.get("/{sensor_id}")
    def retrieve(self, sensor_id : str):
        pass
    
    @route.put("/{sensor_id}")        
    def update(self, sensor_id : str, 
               sensor_request : SensorRequestSchema):
        pass
    
    @route.patch("/{sensor_id}")
    def partial_update(self, sensor_id : str, 
                       sensor_request : SensorRequestSchema):
        pass
    
    @route.delete("/{sensor_id}")
    def destroy(self, sensor_id : str):
        pass
    
