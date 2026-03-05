from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'articles'

urlpatterns = [
    path('happy_busday/', views.invite_view, name='article_list'),
    ]
