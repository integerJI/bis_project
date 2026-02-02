# bis_project/urls.py 수정
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # 장고 내장 뷰 가져오기

urlpatterns = [
    path('admin/', admin.site.urls),
    # 로그인/로그아웃 기능 추가
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('', include('core.urls')),
]