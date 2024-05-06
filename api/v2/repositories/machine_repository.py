from api.v2.models import Machine
from api.v2.schemas import MachineSchema


class MachineRepository:
    
    @staticmethod
    def is_machine_exist(request : MachineSchema):
        machine = Machine.objects.filter(
            code = request.code).first()
        
        if machine:
            return True
        
        return False