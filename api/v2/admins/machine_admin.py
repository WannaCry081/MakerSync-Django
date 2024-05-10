from django.contrib import admin
from api.v2.models import Machine


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ("id", "code")
    