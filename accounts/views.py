from django.shortcuts import render
from functools import wraps
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework.exceptions import NotAuthenticated, AuthenticationFailed

from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from .models import *

# Create your views here.
def user_login(request):
    template_name = 'accounts/login.html'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_exist = CustomUser.objects.filter(username=username).exists()
        if user_exist:
            user = authenticate(username=username, password=password)
            if user is not None:
                if (user.user_type == 'Admin' and user.is_active) or user.is_superuser:
                    login(request, user)
                    return redirect('home')
                elif user.user_type == 'Panchayath' and user.is_active:
                    login(request, user)
                    return redirect('home')
                elif user.user_type == 'Muncipality' and user.is_active:
                    login(request, user)
                    return redirect('home')
                elif user.user_type == 'Corporation' and user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    context = {'msg': 'Invalid Username or Password!'}
                    return render(request, template_name, context)
            else:
                context = {'msg': 'Password is incorrect!'}
                return render(request, template_name, context)
        else:
            context = {'msg': 'User Does Not exist'}
            return render(request, template_name, context)
    return render(request, template_name)