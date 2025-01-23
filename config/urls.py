from django.contrib import admin
from django.http import Http404
from django.shortcuts import render
from django.urls import path, include


from config.fake_db import user_db
from bookmark import views
from todo.views import todo_list, todo_info, todo_create, todo_update, todo_delete
from users import views as user_views

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
    path('todo/create/', todo_create, name='todo_create'),
    path('todo/<int:todo_id>/', todo_info, name='todo_info'),
    path('todo/<int:todo_id>/update/', todo_update, name='todo_update'),
    path('todo/<int:todo_id>/delete/', todo_delete, name='todo_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', user_views.login, name = 'login'),
    path('accounts/signup/', user_views.sign_up, name = 'signup'),

    path('cbv/', include('todo.urls')),
]
