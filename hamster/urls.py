# hamster/urls.py
from django.urls import path
from . import views

app_name = 'hamster' # 네임스페이스 지정

urlpatterns = [
    path('', views.index, name='index'),
    path('main/', views.hamster_main, name='main'),
]