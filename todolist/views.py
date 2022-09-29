from urllib import response
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from http.client import HTTPResponse
import datetime
from django.contrib.auth.decorators import login_required

from todolist.models import ToDoList

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_todolist_items = ToDoList.objects.filter(user=request.user)
    context = {
        'list_item': data_todolist_items,
    }
    return render(request, "todolist.html",context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')


def create_task(request):
    if request.method == 'POST':
        ToDoList.objects.create(user=request.user, date=datetime.datetime.now(),title=request.POST.get('title'),description=request.POST.get('description'),is_finished=False)
        response = HttpResponseRedirect(reverse('todolist:show_todolist'))
        return response
    return render(request, "create_task.html")

def finished_task(request,task_selected):
    status = ToDoList.objects.get(id=task_selected)
    
    if status.is_finished == False:
        status.is_finished == True
    else:
        status.is_finished == False

    status.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

def delete_task(request, id):
    ToDoList.objects.get(id=id).delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))