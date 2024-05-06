from ninja_extra import (
    api_controller, route, ControllerBase)


@api_controller("/machines")
class MachineController(ControllerBase):
    
    @route("/")
    def create(self):  
        pass