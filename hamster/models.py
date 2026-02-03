# hamster/models.py
from django.db import models
from django.contrib.auth.models import User

class Hamster(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, unique=True)
    
    # 레벨 관련 필드 추가
    level = models.IntegerField(default=1) # 이 줄이 없어서 에러가 났던 거예요!
    exp = models.IntegerField(default=0)
    
    # 상태치
    hunger = models.IntegerField(default=100)
    happiness = models.IntegerField(default=100)
    cleanliness = models.IntegerField(default=100)
    
    hamster_type = models.CharField(max_length=20, default="정글리안")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name