from api.v1.schemas import UserRequestSchema, UserResponseSchema
from api.v1.repositories import UserRepository
from api.v1.exceptions import BadRequestException, NotFoundException, ServerErrorException
class UserService:
    
    @staticmethod    
    def list(self, sensor_id : str):
        pass
    
    
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
    def retrieve(self, sensor_id : str, user_email : str):
        pass
    
    
    @staticmethod    
    def update(self, sensor_id : str, user_email : str):
        pass
    
    
    @staticmethod    
    def destroy(self, sensor_id : str, user_email : str):
        pass