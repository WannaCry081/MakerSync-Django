from api.v2.models import Machine


class MachineRepository:
    
    @staticmethod
    def is_machine_exist(code : str):
        machine = Machine.objects.filter(
            code = code).first()
        
        if machine:
            return True
        
        return False
    
    
    @staticmethod
    def create_machine(code : str):
        machine = Machine.objects.create(
            code = code)

        return True