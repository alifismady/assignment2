from django.urls import path
from todolist.views import show_todolist
from todolist.views import register, login_user, logout_user, create_task, finished_task, delete_task, show_todolist_json, create_for_modal


app_name = 'todolist'

urlpatterns = [
    path('',show_todolist,name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_task/', create_task, name='create_task'),
    path('finished_task/<int:task_selected>',finished_task,name='finished_task'),
    path('delete/<int:id>', delete_task, name='delete_task'),
    path('json/', show_todolist_json, name='show_todolist_json'),
    path('add/', create_for_modal, name='create_for_modal')
]