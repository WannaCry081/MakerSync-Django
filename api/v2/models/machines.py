from django.db import models


class Machine(models.Model):
    
    code = models.CharField(
        max_length = 50, unique = True)
    
    created_at = models.DateTimeField(
        auto_now_add = True)
    updated_at = models.DateTimeField(
        auto_now = True)
    
    
    def __str__(self):
        return self.code