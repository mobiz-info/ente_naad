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
import json

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


def select_government(request):
    gbody = request.GET.get('gbodyid')
    dis=request.GET.get('dis_id')
    print(dis,"dis")
    print("hisree", gbody)
    if gbody == "panchayath":
        rec = list(Panchayath.objects.filter(district=dis).values('Panchayath_id', 'name'))
    elif gbody == "muncipality":
        breakpoint()
        rec = list(Muncipality.objects.filter(district=dis).values('muncipality_id', 'name'))
    else:
        rec = list(Corporation.objects.filter(district=dis).values('corporation_id', 'name'))

    data = [{'id': item['Panchayath_id'] if gbody == 'panchayath' else item['muncipality_id'] if gbody == 'muncipality' else item['corporation_id'],
             'name': item['name']} for item in rec]
    print(data,"data")
    return JsonResponse({'data': data})
    

def ward_Adding(request):
    form = Ward_Add_Form
    template_name = 'master/add_ward.html'
    context = {'form': form}
    gbody = request.POST.get('gbody')
   
    gname = request.POST.get('gname')
  
   
    if request.method == 'POST':
        form = Ward_Add_Form(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            if gbody == "panchayath":
                panc_id=Panchayath.objects.get(Panchayath_id=gname)
                
                data.panchayath=panc_id
                data.governing_body='Panchayath'
            elif gbody == 'corporation':
                cor_id=Corporation.objects.get(corporation_id=gname)

                data.corporation=cor_id
                data.governing_body='Corporation'
            else:
                mun_id=Muncipality.objects.get(muncipality_id=gname)
                data.muncipality=mun_id
                data.governing_body='Muncipality'

            data.save()
            messages.success(request, 'Ward Successfully Added.', 'alert-success')
            return redirect('ward_list')
        else:
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)

    
  

def ward_list(request):
    template_name = 'master/ward_list.html'
    ward_list = Ward.objects.all()
    context = {'ward_list': ward_list}
    return render(request, template_name, context)


def ward_edit(request, ward_id):
   
    try:
        ward = Ward.objects.get(ward_id=ward_id)
    except Ward.DoesNotExist:
        messages.error(request, 'Ward not found.', 'alert-danger')
        return redirect('ward_list')

    if request.method == 'POST':
        form = Ward_Add_Form(request.POST, instance=ward)
        gbody = request.POST.get('gbody')
        gname = request.POST.get('gname')

        if form.is_valid():
            data = form.save(commit=False)
            if gbody == "panchayath":
                try:
                    panc_id = Panchayath.objects.get(Panchayath_id=gname)
                    data.panchayath = panc_id
                    data.governing_body = 'Panchayath'
                except Panchayath.DoesNotExist:
                    messages.error(request, 'Panchayath not found.', 'alert-danger')
                    return render(request, 'master/edit_ward.html', {'form': form})
            elif gbody == 'corporation':
                try:
                    cor_id = Corporation.objects.get(corporation_id=gname)
                    data.corporation = cor_id
                    data.governing_body = 'Corporation'
                except Corporation.DoesNotExist:
                    messages.error(request, 'Corporation not found.', 'alert-danger')
                    return render(request, 'master/edit_ward.html', {'form': form})
            else:
                try:
                    mun_id = Muncipality.objects.get(muncipality_id=gname)
                    data.muncipality = mun_id
                    data.governing_body = 'Muncipality'
                except Muncipality.DoesNotExist:
                    messages.error(request, 'Muncipality not found.', 'alert-danger')
                    return render(request, 'master/edit_ward.html', {'form': form})

            data.save()
            messages.success(request, 'Ward Successfully Updated.', 'alert-success')
            return redirect('ward_list')
        else:
            messages.error(request, 'Data is not valid.', 'alert-danger')
            return render(request, 'master/edit_ward.html', {'form': form})
    else:
        form = Ward_Add_Form(instance=ward)
        return render(request, 'master/edit_ward.html', {'form': form})

def ward_delete(request):
    print("hhh")
    pk = request.GET.get('delete_id')
    rec = Ward.objects.get(ward_id=pk)
    
    rec.delete()
    return redirect('ward_list')


def dep_list(request):
    template_name = 'master/dep_list.html'
    dep_list = Department.objects.all()
    context = {'dep_list': dep_list}
    return render(request, template_name, context)

def department_add(request):
    form = Dep_Adding_Form
    template_name = 'master/dep_add.html'
    context = {'form': form}
    if request.method == 'POST':
        form = Dep_Adding_Form(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'Department Successfully Added.', 'alert-success')
            return redirect('dep_list')
        else:
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)
def dep_edit(request, pk):
    template_name = 'master/edit_dep.html'
    ser_rec = Department.objects.get(department_id=pk)
    form = Dep_Edit_Form(instance=ser_rec)
    context = {'form': form}
    if request.method == 'POST':
        form = Dep_Edit_Form(request.POST, request.FILES, instance=ser_rec)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, 'Department Successfully Updated.', 'alert-success')
            return redirect('dep_list')
        else:
            print(form.errors)
            messages.success(request, 'Data is not valid.', 'alert-danger')
            context = {'form': form}
            return render(request, template_name, context)
    else:
        return render(request, template_name, context)
    

def dep_delete(request):
    print("hhh")
    pk = request.GET.get('delete_id')
    rec = Department.objects.get(department_id=pk)
    
    rec.delete()
    return redirect('dep_list')




def allocate_dep_page(request):
    template_name = 'master/dep_allocate_location.html'
    dis_obj=District.objects.all().values('district_id','name')
    context={'dis_obj':dis_obj}
    return render(request, template_name,context)
def allocate_dep(request):
    template_name = 'master/dep_allocate_location.html'

    try:
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        
        selected_departments = body_data.get('selectedDepartments', [])
        gbody= body_data.get('gbodyid')
        
        districtid=body_data.get('districtid')
        pan_mun_cor_id=body_data.get('pan_mun_cor_id')
        
        for department_id in selected_departments:
           
            if  gbody == "panchayath":
                print("llll")
                Department_Allocation.objects.create(
                    panchayath= Panchayath.objects.get(Panchayath_id=pan_mun_cor_id),
                    district=District.objects.get(district_id=districtid),
                    deparment=Department.objects.get(department_id=department_id.get('department_id'))
                )
            if  gbody == "corporation":
              
                Department_Allocation.objects.create(
                    muncipality= Corporation.objects.get(corporation_id=pan_mun_cor_id),
                    district=District.objects.get(district_id=districtid),
                    deparment=Department.objects.get(department_id=department_id.get('department_id'))
                )
            if  gbody == "muncipality":
            
                Department_Allocation.objects.create(
                    muncipality= Muncipality.objects.get(muncipality_id=pan_mun_cor_id),
                    district=District.objects.get(district_id=districtid),
                    deparment=Department.objects.get(department_id=department_id.get('department_id'))
                )
        messages.success(request, 'Department Successfully Allocated.', 'alert-success')
        return render(request, template_name)
        
    except Exception as e:
        print(f"Error: {e}")
        messages.error(request, 'Something went wrong, please try again later!', 'alert-danger')
        return render(request, template_name)
# ajax
def get_dep_data(request):
    if request.method == "GET":
    
        dep_obj = list(Department.objects.all().values('department_id','department_name'))
      
        dat = {'dep_obj': dep_obj}
        return JsonResponse(dat)