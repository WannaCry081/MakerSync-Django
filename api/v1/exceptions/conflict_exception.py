class ConflictException(Exception):
    
    def __init__(self, status = 409, detail = "Conflict Exception"):
        self.status = status
        self.detail = detail
        
        super().__init__()