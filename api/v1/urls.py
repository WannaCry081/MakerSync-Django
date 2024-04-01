from django.urls import path
from ninja import Redoc
from ninja_extra import NinjaExtraAPI


api = NinjaExtraAPI(docs=Redoc())


urlpatterns = [
    path("v1/", api.urls)
]
