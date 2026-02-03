# hamster/models.py
from django.db import models
from django.contrib.auth.models import User

class Hamster(models.Model):
    # 유저 한 명당 햄스터 한 마리 (유저네임 = 햄스터 이름)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True) # 중복 불가 고유 KEY
    
    # 케이지 상태 정보
    exp = models.IntegerField(default=0)
    hunger = models.IntegerField(default=100)
    happiness = models.IntegerField(default=100)
    cleanliness = models.IntegerField(default=100)
    
    # 햄스터 종류나 색상 등 (나중에 확장)
    hamster_type = models.CharField(max_length=20, default="정글리안")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name