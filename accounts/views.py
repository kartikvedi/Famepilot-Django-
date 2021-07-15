from django.shortcuts import render,redirect
from .serializers import *
from .models import *
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

    )
from django.http import HttpResponse, HttpResponseRedirect, Http404
import os
# Create your views here.

def authenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect('dashboard')
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func

@authenticated_user
def homepage(request):
    return render(request,'homepage.html')


@authenticated_user
def register(request):
    if request.method=='POST':
        try:
            us=User.objects.create_user(
                username=request.POST['username'],
                email=request.POST['email'],
                password=request.POST['password'],
            )
            us.save()
            Account.objects.create(
                user=us,
                dob=request.POST['dob'],
                tel=request.POST['tel']
            )
            messages.info(request,'user created')
            return redirect('login')
        except ValidationError  as e:
            messages.info(request,e)
        except :
            messages.info(request,'User already exists/Enter correct details')


    else :
        messages.info(request,'something went wrong')
    return render(request,'register.html')

@authenticated_user
def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            messages.info(request, 'Username/Password is INCORRECT ')

    context = {}
    return render(request, 'login.html', context)

@login_required
def dashboard(request):
    try:
        account=Account.objects.get(user=request.user)
    except:
        account=None

    snippet=AccoutDetailSerializer(account)

    context={'account':account,'snippet': snippet.data}
    return render(request,'dashboard.html',context)

def logout_view(request):
    logout(request)
    return redirect("login")

def download_task1(request):
    if os.path.exists(os.path.join(settings.BASE_DIR,'task1.py')):
        with open(os.path.join(settings.BASE_DIR,'task1.py'),'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-Disposition'] ='inline;filename='+os.path.basename('task1.py')
            return  response
    else: Http404

def download_task2(request):
    if os.path.exists(os.path.join(settings.BASE_DIR,'task2.py')):
        with open(os.path.join(settings.BASE_DIR,'task2.py'),'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/adminupload")
            response['Content-Disposition'] ='inline;filename='+os.path.basename('task2.py')
            return  response
    else: Http404
