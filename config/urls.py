from django.contrib import admin
from django.http import Http404
from django.shortcuts import render
from django.urls import path
from config.fake_db import user_db
from bookmark import views
from todo.views import todo_list, todo_info

_db = {key: value for key, value in user_db.items()}


def user_list(request):
    names = [{'id': key, 'name': value['이름']} for key, value in _db.items()]
    return render(request, 'user_list.html', {'data': names})


def user_info(request, user_id):
    if user_id > len(_db):
        raise Http404('User not found')
    info = _db[user_id]
    return render(request, 'user_info.html', {'data': info})


urlpatterns = [
    # path('users/', user_list, name='user_list'),
    # path('users/<int:user_id>/', user_info, name='user_info'),
    path('admin/', admin.site.urls),
    path('bookmark/', views.bookmark_list),
    path('bookmark/<int:pk>/', views.bookmark_detail ),
    path('todo/', todo_list, name='todo_list'),
    path('route/<int:todo_id>/', todo_info, name='todo_info'),

]
