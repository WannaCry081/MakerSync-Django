from django.urls import path
from ninja import Redoc
from ninja_extra import NinjaExtraAPI
from api.v1.controllers import *


api=NinjaExtraAPI()
api.register_controllers(
    SensorController
)

urlpatterns = [
    path("v1/", api.urls)
]
