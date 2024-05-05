from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from api.v2.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    
    def get_fieldsets(self, request, obj = None):
        
        fieldsets = super().get_fieldsets(request, obj)
        print(fieldsets)
        # if obj:
        #     fieldsets = (
        #         (None, {"fields" : ("email", "password")})
        #     ) + fieldset
        
        return fieldsets
            