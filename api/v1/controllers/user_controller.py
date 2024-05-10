from pydantic import EmailStr
from typing import List
from ninja_extra import (
    ControllerBase, api_controller, route)
from api.v1.schemas import (
    UserSchema, ErrorSchema)
from api.v1.exceptions import (
    BadRequestException, NotFoundException, 
    ServerErrorException, ConflictException)
from api.v1.services import UserService


@api_controller("/machines/{machine_code}/users")
class UserController(ControllerBase):
    
    @route.get("/", 
               summary="List Users",
               description="Retrieve a list of users for a given sensor ID.",
               response={
                   200: List[UserSchema],
                   404: ErrorSchema,
                   500: ErrorSchema,
               })
    def list(self, machine_code: str):
        """
        Retrieve a list of users for a given sensor ID.
        """
        try:
            response = UserService.list(machine_code)
            return 200, response
        except NotFoundException as e:
            return 404, ErrorSchema(
               **e.__dict__)
        except:
            return 500, ErrorSchema(
                **ServerErrorException().__dict__)
            

    @route.post("", 
                summary="Create User",
                description="Create a new user for a given sensor ID.",
                response={
                    201: UserSchema,
                    400: ErrorSchema,
                    500: ErrorSchema
                })
    def create(self, machine_code: str, user_request: UserSchema):
        """
        Create a new user for a given sensor ID.
        """
        try:
            response = UserService.create(machine_code, user_request)
            return 201, response
        except BadRequestException as e:
            return 400, ErrorSchema(
               **e.__dict__)
        except NotFoundException as e:
            return 404, ErrorSchema(
               **e.__dict__)
        except ConflictException as e:
            return 409, ErrorSchema(
               **e.__dict__)
        except:
            return 500, ErrorSchema(
                **ServerErrorException().__dict__)
            
        
    @route.get("/{email}", 
               summary="Retrieve User",
               description="Retrieve user details by email address for a given sensor ID.",
               response={
                   200: UserSchema,
                   400: ErrorSchema,
                   404: ErrorSchema,
                   500: ErrorSchema
               })
    def retrieve(self, machine_code: str, email: EmailStr):
        """
        Retrieve user details by email address for a given sensor ID.
        """
        try: 
            response = UserService.retrieve(machine_code, email)
            return 200, response
        except BadRequestException as e:
            return 400, ErrorSchema(
               **e.__dict__)
        except NotFoundException as e:
            return 404, ErrorSchema(
               **e.__dict__)
        except:
            return 500, ErrorSchema(
                **ServerErrorException().__dict__)
            
        
    @route.put("/{email}", 
               summary="Update User",
               description="Update user details by email address for a given sensor ID.",
               response={
                   200: UserSchema,
                   400: ErrorSchema,
                   404: ErrorSchema,
                   500: ErrorSchema
               })
    def update(self, machine_code: str, email: EmailStr, user_request: UserSchema):
        """
        Update user details by email address for a given sensor ID.
        """
        try: 
            response = UserService.update(machine_code, email, user_request)
            return 200, response
        except BadRequestException as e:
            return 400, ErrorSchema(
               **e.__dict__)
        except NotFoundException as e:
            return 404, ErrorSchema(
               **e.__dict__)
        except:
            return 500, ErrorSchema(
                **ServerErrorException().__dict__)
            
        
    @route.delete("/{email}", 
                  summary="Delete User",
                  description="Delete user by email address for a given sensor ID.",
                  response={
                      204: dict,
                      404: ErrorSchema,
                      500: ErrorSchema
                  })
    def destroy(self, machine_code: str, email: EmailStr):
        """
        Delete user by email address for a given sensor ID.
        """
        try: 
            response = UserService.destroy(machine_code, email)
            return 204, {"detail": "User successfully deleted."}
        except NotFoundException as e:
            return 404, ErrorSchema(
               **e.__dict__)
        except ServerErrorException as e:
            return 500, ErrorSchema(
                **ServerErrorException().__dict__)
