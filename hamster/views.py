from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Hamster

# 1. 첫 화면: 닉네임(햄스터 이름) 결정 및 가입
def index(request):
    # 이미 로그인된 상태라면 바로 케이지(메인)로 보냄
    if request.user.is_authenticated:
        return redirect('hamster:main')
    
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        
        # [백엔드 검증] 닉네임 중복 체크 (User 테이블의 username과 매칭)
        if User.objects.filter(username=nickname).exists():
            return render(request, 'hamster/index.html', {
                'error': '이미 그 이름으로 살고 있는 햄찌가 있어요! 다른 이름을 지어주세요.'
            })
        
        # 1. 유저 생성 (비밀번호는 암호화되어 저장됨)
        user = User.objects.create_user(username=nickname, password=password)
        
        # 2. 햄스터 생성 (유저네임과 햄스터 이름을 동일하게 설정)
        Hamster.objects.create(
            owner=user, 
            name=nickname,
            hunger=100,     # 초기 포만감
            happiness=100   # 초기 행복도
        )
        
        # 3. 생성과 동시에 로그인 처리
        login(request, user)
        
        # 4. 케이지(메인 화면)로 리다이렉트
        return redirect('hamster:main')
        
    return render(request, 'hamster/index.html')


# 2. 메인 화면: 햄스터 케이지 뷰
@login_required
def hamster_main(request):
    try:
        # 현재 로그인한 유저의 햄스터 정보를 가져옴
        hamster = Hamster.objects.get(owner=request.user)
    except Hamster.DoesNotExist:
        # 혹시나 햄스터 정보가 없는 경우를 대비한 예외 처리
        return redirect('hamster:index')
        
    return render(request, 'hamster/main.html', {'hamster': hamster})


@login_required
def feed_hamster(request):
    if request.method == 'POST':
        hamster = Hamster.objects.get(owner=request.user)
        hamster.hunger = min(hamster.hunger + 15, 100) # 포만감 +15
        hamster.happiness = min(hamster.happiness + 5, 100) # 행복도 +5
        hamster.save()
    return redirect('hamster:main')

@login_required
def play_hamster(request):
    if request.method == 'POST':
        hamster = Hamster.objects.get(owner=request.user)
        hamster.exp += 20 # 경험치 +20
        hamster.happiness = min(hamster.happiness + 10, 100)
        hamster.hunger = max(hamster.hunger - 10, 0) # 운동하면 배고파짐
        
        # 레벨업 로직 (경험치 100마다 레벨업)
        if hamster.exp >= 100:
            hamster.level += 1
            hamster.exp = 0
            
        hamster.save()
    return redirect('hamster:main')