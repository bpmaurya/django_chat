from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.forms.widgets import EmailInput
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignUpForm
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
# Create your views here.


def home(request):
    return render(request, 'chat/home.html')


def about(request):
    return render(request, 'chat/about.html')


def contact(request):
    return render(request, 'chat/contact.html')



def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(
                request, 'Congratulations you have become an author')
            user = form.save()
            # group = Group.objects.get(name='Author')
            # user.groups.add(group)
            form = SignUpForm()
    else:
        form = SignUpForm()
    return render(request, 'chat/signup.html', {'form':form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully!!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'chat/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                pst = Post(title=title,desc=desc)
                pst.save()
                messages.success(request, 'Post added successfully!!')
                form = PostForm()
        else:
            form = PostForm()
        return render(request, 'chat/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')






def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')





# chat/views.py
from django.shortcuts import render

def index(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully!!')
                    return HttpResponseRedirect('/chat/')
        else:
            form = LoginForm()
        return render(request, 'chat/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/chat/')
    
    # return render(request, 'chat/index.html', {})
def index1(request):
    return render(request, 'chat/index.html')





def room(request, room_name):
    if request.user.is_authenticated:
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'chat/room.html', {'room_name': room_name ,'full_name':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')
    # return render(request, 'chat/room.html', {
    #     'room_name': room_name
    # })    