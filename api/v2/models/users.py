from django.db import models
from api.v2.models import Machine


class User(models.Model):
    
    email = models.EmailField(unique = True, blank = False, null = False)
    password = models.CharField(max_length = 150)
    machine = models.ForeignKey(Machine, on_delete = models.CASCADE, blank = False)

    
    def __str__(self):
        return self.email