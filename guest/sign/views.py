from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "index.html")
    #return HttpResponse("Hello Django!")

# action of login
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # 登录
            auth.login(request, user)
            # 将session信息记录到浏览器
            request.session['user'] = username
            # 重定向到/event_manage/目录
            response = HttpResponseRedirect('/event_manage/')
            # 添加浏览器cookie
            #response.set_cookie('user', username, 3600)
            return  response
        else:
            return render(request, 'index.html', {'error': "username or password error!"})

# 发布会管理
@login_required
def event_manage(request):
    # 读取浏览器cookie
    #username = request.COOKIES.get('user', '')
    # 读取浏览器session
    username = request.session.get('user', '')
    return render(request, "event_manage.html", {"user": username})
