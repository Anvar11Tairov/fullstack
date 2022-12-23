from django.http import HttpResponse
import models
from .models import Services, Feddback, Fullfb, Staff
from django.shortcuts import render
from django import forms
from .forms import FeedBackForm
from django.forms import ModelForm
from django.shortcuts import redirect
import django
# f = ArticleForm(request.POST)
# new_article = f.save()
def save_model(self, request, obj, form, change):
    super(PostAdmin, self).save_model(self, request, obj, form)

def home(request):
        staff = Staff.objects.all()
        form = FeedBackForm(request.POST or None)
        if form.is_valid():
            # services.save() -- это работает
            form.save()
            # form.save(commid = True)
            return redirect('/')
        services = Services.objects.all()
        return render(request, 'index.html', context={"services": services, "staff":staff,  "form":form})

def service(request):
     return render(request, 'servise.html')

def getService(request, id):
    product = Services.objects.get(id=id)
    return render(request, 'product.html', context={"product":product})

def exam(request):
    return render(request, 'exam.html')

def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    return render(request, "index.html")

def login(request):
    if request.method == "POST":
        request.POST.get("login") == username
        return redirect('index.html')
    return render(request, 'login.html')

def team(request):
    return render(request, 'team.html')