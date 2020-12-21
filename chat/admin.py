from django.contrib import admin

# Register your models here.
from .models import User

@admin.register(User)    
class UserModelAdmin(admin.ModelAdmin):
    list_display=['id','username','first_name','last_name','email','password']
