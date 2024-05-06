from ninja_extra import (
    api_controller, ControllerBase, route)


@api_controller("/machines/{code}/sensors")
class SensorController(ControllerBase):
    pass