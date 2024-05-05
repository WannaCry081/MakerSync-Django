from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    
    username = None
    first_name = None
    last_name = None
    
    email = models.EmailField(unique = True, blank = False, null = False)

    USERNAME_FIELD = "email"
    
    
    def __str__(self):
        return self.email