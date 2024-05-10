import os
from dotenv import load_dotenv
from django.urls import path
from ninja import Redoc, Swagger
from ninja_extra import NinjaExtraAPI
from api.v1.controllers import (
    UserController,
    MachineController
)


load_dotenv()

docs = Swagger() 
environment = os.environ.get("DJANGO_ENV")

if environment.lower() != "development":
    docs = Redoc()
    
api = NinjaExtraAPI(
    title = "MakerSyncAPI",
    description = "A Semi-automation PETG Material to 3D Printing Filament Application Programming Interface that establish a connection to the ESP32 and Firebase for a seamless interaction between our Mobile Application developed in Flutter.",
    version = "1.1", 
    docs = docs
)

api.register_controllers(
    UserController,
    MachineController
)

urlpatterns = [
    path("v1/", api.urls)
]
