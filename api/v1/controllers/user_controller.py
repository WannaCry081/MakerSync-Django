from ninja_extra import ControllerBase, api_controller, route
from api.v1.schemas import UserRequestSchema, UserResponseSchema, ErrorResponseSchema
from api.v1.services import UserService
from api.v1.exceptions import BadRequestException, NotFoundException, ServerErrorException


@api_controller("/users")
class UserController(ControllerBase):
    
    @route.get("/{sensor_id}")
    def list(self, sensor_id : str):
        pass
    
    
    @route.post("/{sensor_id}", response={
        201: UserResponseSchema,
        400: ErrorResponseSchema,
        500: ErrorResponseSchema
    })
    def create(self, sensor_id : str, user_request: UserRequestSchema):
        try:
            response = UserService.create(sensor_id, user_request)
            return 201, response
        except BadRequestException as e:
            return 400, ErrorResponseSchema(
                status=e.status,
                detail=e.detail
            )
        except ServerErrorException as e:
            return 500, ErrorResponseSchema(
                status=e.status,
                detail=e.detail
            )
        
    
    
    @route.get("/{sensor_id}/{user_email}")
    def retrieve(self, sensor_id : str, user_email : str):
        pass
    
    
    @route.put("/{sensor_id}/{user_email}")
    def update(self, sensor_id : str, user_email : str):
        pass
    
    
    @route.delete("/{sensor_id}/{user_email}")
    def destroy(self, sensor_id : str, user_email : str):
        pass