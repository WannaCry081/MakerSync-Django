from api.v1.schemas import UserRequestSchema, UserResponseSchema
from api.v1.repositories import UserRepository
from api.v1.exceptions import BadRequestException, NotFoundException, ServerErrorException
class UserService:
    
    @staticmethod    
    def list(sensor_id : str):

        users_data=UserRepository.get_users(sensor_id)
        if not users_data:
            raise NotFoundException(
                detail="No users found."
            )
        try:
            users = {idx: dict(user_data) for idx, user_data in enumerate(users_data, start=1)}
            print(users)
        except Exception as e:
            print("Error during instantiation:", e)

        # users=[UserResponseSchema(**user_data) for user_data in users_data]
        
        return users
    
    
    @staticmethod    
    def create(sensor_id : str, user_request: UserRequestSchema):
        
        email=user_request.email
        if UserRepository.is_user_exists(sensor_id, email):
            raise BadRequestException(
                detail="User already exists."
            )
        
        if not UserRepository.create_user(sensor_id, user_request):
            raise ServerErrorException()
        
        return UserResponseSchema(**user_request.dict())
    
    
    @staticmethod    
    def retrieve(sensor_id : str, email : str):
        
        if not UserRepository.is_user_exists(sensor_id, email):
            raise NotFoundException(
                detail="User does not exist."
            )
        
        user=UserRepository.get_user(sensor_id, email)
        if not user:
            raise BadRequestException(
                detail="Invalid user email."
            )
        
        return UserResponseSchema(**user)

    
    
    @staticmethod    
    def update(sensor_id : str, email: str, user_request : UserRequestSchema):
        
        if not UserRepository.get_user(sensor_id, email):
            raise NotFoundException(
                detail="User not found."
            )
        
        user=UserRepository.update_user(sensor_id, email, user_request)
        if not user:
            raise BadRequestException(
                detail="Invalid request."
            )
        
        return UserResponseSchema(**user_request.dict())
    
    
    @staticmethod    
    def destroy(sensor_id : str, email : str):
        
        if not UserRepository.get_user(sensor_id, email):
            raise NotFoundException(
                detail="User not found."
            )
        
        if not UserRepository.delete_user(sensor_id, email):
            raise ServerErrorException()
        
        return True