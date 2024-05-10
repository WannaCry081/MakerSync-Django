from django.db import models
from api.v2.models import Machine


class User(models.Model):
    
    username = models.CharField(
        unique = True, max_length = 100, 
        blank = False, null = False)
    email = models.EmailField(
        unique = True, blank = False,
        null = False)
    machine = models.ForeignKey(
        Machine, on_delete = models.CASCADE, 
        blank = False)

    
    def __str__(self):
        return self.email