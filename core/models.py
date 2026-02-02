from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField(max_length=280) # X(트위터) 글자 수 제한 느낌!
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] # 최신순 정렬

    def __str__(self):
        return f"{self.author.username}: {self.content[:20]}"