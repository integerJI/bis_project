# bis_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('hamster.urls')), 
    
    path('sns/', include('core.urls')), 

    # 인증 관련 (로그인은 core의 템플릿을 그대로 써도 되고, 나중에 hamster로 옮겨도 됩니다)
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]