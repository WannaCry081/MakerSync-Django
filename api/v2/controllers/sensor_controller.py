from ninja_extra import (
    api_controller, ControllerBase, route)
from api.v2.schemas import (
    MachineSchema, SensorSchema)


@api_controller("/machines/{machine_code}/sensors")
class SensorController(ControllerBase):
    
    @route.get("/{sensor_id}")
    def retrieve(self, machine_code : str, sensor_id : int):
        pass
    
    
    @route.post("/")
    def create(self, machine_code : str, request : SensorSchema):
        pass
    
    
    @route.put("/{sensor_id}")
    def update(self, machine_code : str, sensor_id : int, 
               request : SensorSchema):
        pass
    
    
    @route.delete("/{sensor_id}")
    def destroy(self, machine_code : str, sensor_id : int):
        pass