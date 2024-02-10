
from django.contrib import admin
from django.urls import path, include, re_path

from wiki.views import *


urlpatterns = [
    path('admin/', admin.site.urls), #админка
    path('api/v1/articles/', ArticlesAPIList.as_view()), # GET получение всех статей и POST добавление статей
    path('api/v1/myarticles/', MyArticlesAPIList.as_view()), # GET получение собственных статей
    path('api/v1/articlesfound/<int:pk>/', ArticlesAPIUpdate.as_view()), # обновление статей
    path('api/v1/articlessearch/<int:owner>/', ArticlesAPIDetailView.as_view()), # получение статей по id пользователя
    path('api/v1/articlesdelete/<int:pk>/', ArticlesAPIDestroy.as_view()), # удаление статей
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),


]
# http://127.0.0.1:8000/api/v1/auth/users/ POST регестрация/ GET получение списка пользователей
# http://127.0.0.1:8000/auth/token/login/  POST получение токена username,password
# http://127.0.0.1:8000/api/v1/articles/   GET получение всех статей is_published=True / POST добавление статей