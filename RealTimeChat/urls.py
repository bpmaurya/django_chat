
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from chat import views
urlpatterns = [
     path('admin/', admin.site.urls),
    path('',views.home,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('signup/',views.user_signup,name='signup'),
    # path('login/',views.user_login,name='login'),
    path('login/',views.index,name='login'),
    path('logout/',views.user_logout,name='logout'),

    #this is for chat 
    path('chat/', include('chat.urls')),
]
