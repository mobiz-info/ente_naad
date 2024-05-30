from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import *
from .models import *
from accounts.models import *
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def home(request):
    template_name = 'master/dashboard.html'
   
    return render(request, template_name)



def panchayath_list(request):
    template_name = 'master/panchayath_list.html'
    panchayath_list = Panchayath.objects.all()
    context = {'panchayath_list': panchayath_list}
    return render(request, template_name, context)


def Panchayath_Adding(request):
    form = Panchayath_Add_Form
    template_name = 'master/add_panchayath.html'
    context = {'form': form}
    if request.method == 'POST':
        form = Panchayath_Add_Form(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            password = request.POST.get('pswd')
            data.password = password
           
            passwords = make_password(password)
            email = data.email
            if CustomUser.objects.filter(username=data.username).exists():
                messages.success(request, 'Username already exists. Please choose a different username.', 'alert-danger')
                context = {'form': form}
                return render(request, template_name, context)
            else:  
                custom_user_data = CustomUser.objects.create(password=passwords, username=data.username,
                                first_name=data.username,email=email,user_type='Panchayath')
                data.user = custom_user_data
                data.status = 'Active'
                data.password=password
                data.save()
                messages.success(request, 'Panchayath Successfully Added.', 'alert-success')
                return redirect('panchayath_list')
        else:
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)


def Panchayath_editing(request,pk):
   
    template_name = 'master/edit_panchayath.html'
    rec = Panchayath.objects.get(Panchayath_id=pk)
    print(rec.password)
    form = Panchayath_Edit_Form(instance=rec)
    context = {'form': form,'rec': rec}
    get_new_password = request.POST.get('new_pass_name')
   
    new_password = make_password(get_new_password)
    rec = Panchayath.objects.get(Panchayath_id=pk)

    if request.method == 'POST':
        form = Panchayath_Edit_Form(request.POST, instance=rec)
   
        if form.is_valid():
            data = form.save(commit=False)
            custom_user_data = CustomUser.objects.filter(id=rec.user.id).update(first_name=data.username,
                                                                            username=data.username,
                                                                                user_type='Panchayath',
                                                                                password=new_password,
                                                                                email=data.email)
            data.password = get_new_password
            data.save()

            messages.success(request, 'Panchayath Data Successfully Updated', 'alert-success')
            return redirect('panchayath_list')
        else:
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request,template_name, context)
        
    else:
        return render(request, template_name, context)
    



def panchayath_delete(request):
    pk = request.GET.get('delete_id')
    rec = Panchayath.objects.get(Panchayath_id=pk)
    
    rec.delete()
    return redirect('panchayath_list')

################################corporation####################################

def corporation_Adding(request):
    form = Corporation_Add_Form
    template_name = 'master/add_corporation.html'
    context = {'form': form}
    if request.method == 'POST':
        form = Corporation_Add_Form(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            password = request.POST.get('pswd')
            data.password = password
           
            passwords = make_password(password)
            email = data.email
            if CustomUser.objects.filter(username=data.username).exists():
                messages.success(request, 'Username already exists. Please choose a different username.', 'alert-danger')
                context = {'form': form}
                return render(request, template_name, context)
            else:  
                custom_user_data = CustomUser.objects.create(password=passwords, username=data.username,
                                first_name=data.username,email=email,user_type='Corporation')
                data.user = custom_user_data
                data.status = 'Active'
                data.password=password
                data.save()
                messages.success(request, 'Corporation Successfully Added.', 'alert-success')
                return redirect('corporation_list')
        else:
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)

def corporation_list(request):
    template_name = 'master/corporation_list.html'
    corporation_list = Corporation.objects.all()
    context = {'corporation_list': corporation_list}
    return render(request, template_name, context)


def corporation_editing(request,pk):
   
    template_name = 'master/edit_corporation.html'
    rec = Corporation.objects.get(corporation_id=pk)
    print(rec.password)
    form = Corporation_Edit_Form(instance=rec)
    context = {'form': form,'rec': rec}
    get_new_password = request.POST.get('new_pass_name')
   
    new_password = make_password(get_new_password)
    rec = Corporation.objects.get(corporation_id=pk)

    if request.method == 'POST':
        form = Corporation_Edit_Form(request.POST, instance=rec)
   
        if form.is_valid():
            data = form.save(commit=False)
            custom_user_data = CustomUser.objects.filter(id=rec.user.id).update(first_name=data.username,
                                                                            username=data.username,
                                                                                user_type='Corporation',
                                                                                password=new_password,
                                                                                email=data.email)
            data.password = get_new_password
            data.save()

            messages.success(request, 'Corporation Data Successfully Updated', 'alert-success')
            return redirect('corporation_list')
        else:
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request,template_name, context)
        
    else:
        return render(request, template_name, context)
    



def corporation_delete(request):
    pk = request.GET.get('delete_id')
    rec = Corporation.objects.get(corporation_id=pk)
    
    rec.delete()
    return redirect('corporation_list')


#########################muncipality#####################################

def muncipality_Adding(request):
    form = Muncipality_Add_Form
    template_name = 'master/add_muncipality.html'
    context = {'form': form}
    if request.method == 'POST':
        form = Muncipality_Add_Form(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            password = request.POST.get('pswd')
            data.password = password
           
            passwords = make_password(password)
            email = data.email
            if CustomUser.objects.filter(username=data.username).exists():
                messages.success(request, 'Username already exists. Please choose a different username.', 'alert-danger')
                context = {'form': form}
                return render(request, template_name, context)
            else:  
                custom_user_data = CustomUser.objects.create(password=passwords, username=data.username,
                                first_name=data.username,email=email,user_type='Corporation')
                data.user = custom_user_data
                data.status = 'Active'
                data.password=password
                data.save()
                messages.success(request, 'Muncipality Successfully Added.', 'alert-success')
                return redirect('muncipality_list')
        else:
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)

def muncipality_list(request):
    template_name = 'master/muncipality_list.html'
    muncipality_list = Muncipality.objects.all()
    context = {'muncipality_list': muncipality_list}
    return render(request, template_name, context)


def muncipality_editing(request,pk):
   
    template_name = 'master/edit_muncipality.html'
    rec = Muncipality.objects.get(muncipality_id=pk)
    print(rec.password)
    form = Muncipality_Edit_Form(instance=rec)
    context = {'form': form,'rec': rec}
    get_new_password = request.POST.get('new_pass_name')
   
    new_password = make_password(get_new_password)
    rec = Muncipality.objects.get(muncipality_id=pk)

    if request.method == 'POST':
        form = Muncipality_Edit_Form(request.POST, instance=rec)
   
        if form.is_valid():
            data = form.save(commit=False)
            custom_user_data = CustomUser.objects.filter(id=rec.user.id).update(first_name=data.username,
                                                                            username=data.username,
                                                                                user_type='Corporation',
                                                                                password=new_password,
                                                                                email=data.email)
            data.password = get_new_password
            data.save()

            messages.success(request, 'Muncipality Data Successfully Updated', 'alert-success')
            return redirect('muncipality_list')
        else:
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request,template_name, context)
        
    else:
        return render(request, template_name, context)
    



def muncipality_delete(request):
    pk = request.GET.get('delete_id')
    rec = Muncipality.objects.get(muncipality_id=pk)
    
    rec.delete()
    return redirect('muncipality_list')
