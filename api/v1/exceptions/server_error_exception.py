class ServerErrorException(Exception):
    
    def __init__(self, status=500, detail="Internal Server Error"):
        self.status=status
        self.detail=detail
        
        super().__init__()