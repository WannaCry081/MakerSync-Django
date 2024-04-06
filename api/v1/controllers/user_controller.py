from ninja_extra import ControllerBase, api_controller, route
from api.v1.schemas import UserRequestSchema, UserResponseSchema, ErrorResponseSchema
from api.v1.services import UserService
from api.v1.exceptions import BadRequestException, NotFoundException, ServerErrorException
from typing import List


@api_controller("/users")
class UserController(ControllerBase):
    
    @route.get("/{sensor_id}", 
               summary="List Users",
               description="Retrieve a list of users for a given sensor ID.",
               response={
                   200: List[UserResponseSchema],
                   404: ErrorResponseSchema,
                   500: ErrorResponseSchema,
               })
    def list(self, sensor_id: str):
        """
        Retrieve a list of users for a given sensor ID.
        """
        try:
            response = UserService.list(sensor_id)
            return 200, response
        except NotFoundException as e:
            return 404, ErrorResponseSchema(
                status=e.status,
                detail=e.detail
            )
        except ServerErrorException as e:
            return 500, ErrorResponseSchema(
                status=e.status,
                detail="Internal Server Error"
            )

    @route.post("/{sensor_id}", 
                summary="Create User",
                description="Create a new user for a given sensor ID.",
                response={
                    201: UserResponseSchema,
                    400: ErrorResponseSchema,
                    500: ErrorResponseSchema
                })
    def create(self, sensor_id: str, user_request: UserRequestSchema):
        """
        Create a new user for a given sensor ID.
        """
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
                detail="Internal Server Error"
            )
        
    @route.get("/{sensor_id}/{email}", 
               summary="Retrieve User",
               description="Retrieve user details by email address for a given sensor ID.",
               response={
                   200: UserResponseSchema,
                   400: ErrorResponseSchema,
                   404: ErrorResponseSchema,
                   500: ErrorResponseSchema
               })
    def retrieve(self, sensor_id: str, email: str):
        """
        Retrieve user details by email address for a given sensor ID.
        """
        try: 
            response = UserService.retrieve(sensor_id, email)
            return 200, response
        except BadRequestException as e:
            return 400, ErrorResponseSchema(
                status=e.status,
                detail=e.detail
            )
        except NotFoundException as e:
            return 404, ErrorResponseSchema(
                status=e.status,
                detail=e.detail
            )
        except ServerErrorException as e:
            return 500, ErrorResponseSchema(
                status=e.status,
                detail="Internal Server Error"
            )
        
    @route.put("/{sensor_id}/{email}", 
               summary="Update User",
               description="Update user details by email address for a given sensor ID.",
               response={
                   200: UserResponseSchema,
                   400: ErrorResponseSchema,
                   404: ErrorResponseSchema,
                   500: ErrorResponseSchema
               })
    def update(self, sensor_id: str, email: str, user_request: UserRequestSchema):
        """
        Update user details by email address for a given sensor ID.
        """
        try: 
            response = UserService.update(sensor_id, email, user_request)
            return 200, response
        except BadRequestException as e:
            return 400, ErrorResponseSchema(
                status=e.status,
                detail=e.detail
            )
        except NotFoundException as e:
            return 404, ErrorResponseSchema(
                status=e.status,
                detail=e.detail
            )
        except ServerErrorException as e:
            return 500, ErrorResponseSchema(
                status=e.status,
                detail="Internal Server Error"
            )
        
    @route.delete("/{sensor_id}/{email}", 
                  summary="Delete User",
                  description="Delete user by email address for a given sensor ID.",
                  response={
                      204: dict,
                      404: ErrorResponseSchema,
                      500: ErrorResponseSchema
                  })
    def destroy(self, sensor_id: str, email: str):
        """
        Delete user by email address for a given sensor ID.
        """
        try: 
            response = UserService.destroy(sensor_id, email)
            return 204, {"detail": "User successfully deleted."}
        except NotFoundException as e:
            return 404, ErrorResponseSchema(
                status=e.status,
                detail=e.detail
            )
        except ServerErrorException as e:
            return 500, ErrorResponseSchema(
                status=e.status,
                detail="Internal Server Error"
            )
