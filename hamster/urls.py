# hamster/urls.py
from django.urls import path
from . import views

app_name = 'hamster'

urlpatterns = [
    path('', views.index, name='index'),               # 닉네임 입력 (로그인/가입)
    path('main/', views.hamster_main, name='main'),     # 케이지 메인
    path('feed/', views.feed_hamster, name='feed'),     # 밥 주기 액션
    path('play/', views.play_hamster, name='play'),     # 쳇바퀴 액션
]