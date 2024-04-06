import os
from dotenv import load_dotenv
from django.urls import path
from ninja import Redoc, Swagger
from ninja_extra import NinjaExtraAPI
from api.v1.controllers import UserController, SensorController


load_dotenv()

docs = Swagger() 
environment = os.environ.get("DJANGO_ENV")

if environment.lower() != "development":
    docs = Redoc()
    
api = NinjaExtraAPI(
    version="1.0.0", 
    docs=docs
)

api.register_controllers(
    UserController,
    SensorController
)

urlpatterns = [
    path("v1/", api.urls)
]
