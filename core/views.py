from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.all() # 모든 글 가져오기 (이미 모델에서 최신순 정렬 설정됨)
    return render(request, 'core/post_list.html', {'posts': posts})

@login_required # 로그인한 사람만 글 쓸 수 있게 보호!
def post_create(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Post.objects.create(author=request.user, content=content)
        return redirect('post_list')
    return render(request, 'core/post_create.html')