from ninja_extra import (
    api_controller, ControllerBase, route)
from api.v2.schemas import (
    MachineSchema, SensorSchema)


@api_controller("/machines/{code}/sensors")
class SensorController(ControllerBase):
    
    @route.get("/{sensor_id}")
    def retrieve(self, code : MachineSchema, sensor_id : int):
        pass
    
    
    @route.post("/")
    def create(self, code : MachineSchema, request : SensorSchema):
        pass
    
    
    @route.put("/{sensor_id}")
    def update(self, code : MachineSchema, sensor_id : int, request : SensorSchema):
        pass
    
    
    @route.delete("/{sensor_id}")
    def destroy(self, code : MachineSchema, sensor_id : int):
        pass