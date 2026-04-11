from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
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

def catalog_view(request, catalog_type):
    catalog_type_name = ''

    if catalog_type == 'all':
        service = Service.objects.all()
        catalog_type_name = "Все"
    else:
        service = Service.objects.filter(catalog_type = 'catalog_type')

        catalog_types = service.catalog_types
        
        for ft in catalog_types:
            if ft[0] == catalog_type:
                catalog_type_name = ft[1]
                break

    context = {
        'service_list' : service,
        'catalog_type' : catalog_type_name
    }
    return render(request,'catalog.html', context)

def service_template(request, id):
   service = Service.objects.get(id = id) # конструктор класса
   context = {
       'service' : service
    }
   return render(request, 'service-template.html', context)

def account(request):
  print(request.user.id)
  try:
    context = {
        'username' : request.user.username,
        'first_name' : request.user.first_name,
        'last_name' : request.user.last_name,
        'email': request.user.email,
    }
    return render(request, 'account.html', context)
  except AttributeError:
      return HttpResponse("<h1>401 Unauthorized</h1>", status=401)