from django.contrib import admin

# Register your models here.
from .models import Post,User

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['id','title','desc']
@admin.register(User)    
class UserModelAdmin(admin.ModelAdmin):
    list_display=['id','username','first_name','last_name','email','password']
