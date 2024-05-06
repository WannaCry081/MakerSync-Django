class ConflictException(Exception):
    
    def __init__(self, status = 409, detail = "Conflict Resource"):
        self.status = status
        self.detail = detail
        
        super().__init__()