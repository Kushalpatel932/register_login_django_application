from django.contrib import admin
from .models import register
# Register your models here.
class user_admin(admin.ModelAdmin):
    list_display = ['user_name','user_email','user_phone_no','user_dob']
admin.site.register(register,user_admin)

