import os
from dotenv import load_dotenv
from django.urls import path
from ninja import Redoc, Swagger
from ninja_extra import NinjaExtraAPI
from api.v2.controllers import *

load_dotenv()

docs = Swagger() 
environment = os.environ.get("DJANGO_ENV")

if environment.lower() != "development":
    docs = Redoc()
    
api = NinjaExtraAPI(
    title = "MakerSyncAPI",
    description = "A Semi-automation PETG Material to 3D Printing Filament Application Programming Interface that establish a connection to the ESP32 and SQLite for a seamless interaction between our Mobile Application developed in Flutter.",
    version = "2.0.0", 
    docs = docs
)

api.register_controllers(
    MachineController,
    SensorController,
    UserController,
    NotificationController
)

urlpatterns = [
    path("v2/", api.urls)
]
