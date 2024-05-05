from django.db import models



class Sensor(models.Model):
    
    is_start = models.BooleanField(default = False)
    is_stop = models.BooleanField(default = False)
    is_initialize = models.BooleanField(default = False)
    counter = models.IntegerField(default = 0)
    time = models.IntegerField(default = 0)
    temperature = models.FloatField(default = 0.0)
    
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    