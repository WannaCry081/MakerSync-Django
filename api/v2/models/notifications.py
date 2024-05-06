from django.db import models
from api.v2.models import Machine


class Notification(models.Model):
    
    title = models.CharField(
        max_length = 100, null = False, 
        blank = False)
    content = models.TextField(
        blank = True, null = True)
    datetime = models.DateTimeField(
        auto_now_add = True)
    machine = models.ForeignKey(
        Machine, on_delete = models.CASCADE, 
        blank = True)
    
    
    def __str__(self):
        return self.title 