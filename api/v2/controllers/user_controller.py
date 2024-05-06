from ninja_extra import (
    api_controller, ControllerBase, route)


@api_controller("/machines/{code}/users")
class UserController(ControllerBase):
    pass