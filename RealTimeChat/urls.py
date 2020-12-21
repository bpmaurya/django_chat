
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from chat import views
urlpatterns = [
     path('admin/', admin.site.urls),
    path('',views.home,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('signup/',views.user_signup,name='signup'),
    # path('login/',views.user_login,name='login'),
    path('login/',views.index,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('add_post/',views.add_post,name='addpost'),
    path('updatepost/<int:id>',views.update_post,name='updatepost'),
    path('delete/<int:id>',views.delete_post,name='deletepost'),

    #this is for chat 
    path('chat/', include('chat.urls')),
]
