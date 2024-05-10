from typing import List
from pydantic import EmailStr
from ninja_extra import (
    api_controller, ControllerBase, route)
from api.v2.schemas import (
    MachineSchema, UserSchema, ErrorSchema)
from api.v2.exceptions import (
    NotFoundException, ServerErrorException,
    BadRequestException, ConflictException)
from api.v2.services import UserService


@api_controller("/machines/{machine_code}/users")
class UserController(ControllerBase):
    """
    API Controller for managing users associated with a machine.
    """

    @route.get("/", 
               summary="Retrieves a list of users associated with a machine.", 
               description="Retrieves a list of users associated with a machine identified by the provided machine code.",
               response={
                   200: List[UserSchema],
                   404: ErrorSchema,
                   500: ErrorSchema
               })
    def list(self, machine_code: str):
        """
        Retrieves a list of users associated with a machine.

        Args:
            machine_code (str): The code identifying the machine.

        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            response = UserService.list(machine_code)
            return 200, response
        except NotFoundException as e:
            return 404, ErrorSchema(**e.__dict__)
        except:
            return 500, ErrorSchema(
                **ServerErrorException().__dict__)

    
    @route.get("/{email}",
           summary="Retrieves a specific user associated with a machine.", 
           description="Retrieves a specific user associated with a machine identified by the provided machine code and user email.",
           response={
               200: UserSchema,
               404: ErrorSchema,
               500: ErrorSchema
           })
    def retrieve(self, machine_code: str, email: EmailStr):
        """
        Retrieves a specific user associated with a machine.

        Args:
            machine_code (str): The code identifying the machine.
            email (EmailStr): The email of the user to retrieve.

        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            response = UserService.retrieve(machine_code, email)
            return 200, response
        except NotFoundException as e:
            return 404, ErrorSchema(**e.__dict__)
        except:
            return 500, ErrorSchema(
                **ServerErrorException().__dict__)

    
    @route.post("/", 
            summary="Creates a new user associated with a machine.", 
            description="Creates a new user associated with a machine identified by the provided machine code.",
            response={
                201: UserSchema,
                400: ErrorSchema,
                404: ErrorSchema,
                409: ErrorSchema,
                500: ErrorSchema
            })
    def create(self, machine_code: str, user_request: UserSchema):
        """
        Creates a new user associated with a machine.

        Args:
        - machine_code (str): The code identifying the machine.
        - user_request (UserSchema): The details of the user to be created.

        Returns:
            tuple: A tuple containing status code and response data.
        """
        try:
            response = UserService.create(machine_code, user_request)
            return 201, response
        except BadRequestException as e:
            return 400, ErrorSchema(**e.__dict__)
        except NotFoundException as e:
            return 404, ErrorSchema(**e.__dict__)
        except ConflictException as e:
            return 409, ErrorSchema(**e.__dict__)
        except:
            return 500, ErrorSchema(
                **ServerErrorException().__dict__)

        
    @route.put("/{email}")
    def update(self, machine_code : str, 
               email : EmailStr, user_request : UserSchema):
        try:
            response = UserService.update(
                machine_code, email, user_request)
            return response
        except BadRequestException as e:
            return ErrorSchema(**e.__dict__)
        except NotFoundException as e:
            return ErrorSchema(**e.__dict__)
        except:
            return ErrorSchema(
                **ServerErrorException().__dict__)
        
    
    @route.delete("/{email}")
    def destroy(self, machine_code : str, email : EmailStr):
        
        try:
            response = UserService.destroy(
                machine_code, email)
            return response
        except BadRequestException as e:
            return ErrorSchema(**e.__dict__)
        except NotFoundException as e:
            return ErrorSchema(**e.__dict__)
        except:
            return ErrorSchema(
                **ServerErrorException().__dict__)