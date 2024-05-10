class NotFoundException(Exception):
    
    def __init__(self, status = 404, detail = "Resource Not Found"):
        self.status = status 
        self.detail = detail
        
        super().__init__()