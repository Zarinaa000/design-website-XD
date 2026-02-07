from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Service

def index(request):
    try:
        context = { 'username' : request.user.username }
        return render(request, 'index.html', context)
    except AttributeError as e:
        return render(request, 'index.html')

def auth(request):
    if request.method == "POST" :
        email = request.POST.get('email')
        password = request.POST.get('password')
        # \n (терминальный n) - это перенос строки
        print('Логин: ', email, '\n', 'Пароль: ', password, sep='')

        # Авторизация: здесь ищется зарегистрированный пользователь
        user = authenticate(request, username=email, password=password) 
        if user is not None: #Если пользователь есть 
           print("Нашелся пользователь, ", user.username)
           login(request, user)
           return JsonResponse({'status': 'success'}) 
        else:
            return JsonResponse({'status': 'error'})  
    return render(request, 'auth.html')

def reg(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        birthday = request.POST.get('birthday')
        username = email

        print('Почта: ', email, '\n', 'Пароль: ', password, 'Имя: ', first_name, sep='')

        user = User.objects.create_user(username, email, password)

        login(request,user)

        return JsonResponse({'status': 'success'})

    return render(request, 'reg.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def catalog_view(request):
    catalog = Service.objects.all()
    context = {
        'service_list': catalog,
    }
    return render(request,'catalog.html', context)

def service_template(request, id):
   service = Service.objects.get(id = id)
   context = {
       'service' : service
    }
   return render(request, 'service-template.html', context)