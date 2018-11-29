from django.shortcuts import render, redirect, HttpResponse, reverse
from django.contrib import auth
from index.forms import RegForm
from index import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, AbstractUser


def redir_index(request):
    return redirect(reverse('index:index'))


def index(request):
    print(request.user, type(request.user))
    return render(request, 'index/index.html')


def login(request):
    error_msg = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        # 对提交的数据进行认证
        obj = auth.authenticate(request, username=username, password=pwd)
        if obj:
            # 登录成功
            auth.login(request, obj)
            return redirect('/index')
        else:
            error_msg = '用户名或密码错误'

    # 返回一个页面让登录
    return render(request, 'index/login.html', {'error_msg': error_msg})


def reg(request):
    form_obj = RegForm()
    if request.method == 'POST':
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():


            '''
            第一种创建用户的方法
            form_obj.cleaned_data.pop('re_password')
            models.UserInfo.objects.create_user(**form_obj.cleaned_data)  # 创建普通用户  当我们使用auth的user表时使用命令 User.objects.create_user(**form_obj.cleaned_data),而当我们继承AbstractUser重写userinfo表时,需要重新指定表
            models.UserInfo.objects.create_superuser(**form_obj.cleaned_data, email='')  # 创建超级用户
            '''

            # 另一种创建用户的方法,推荐
            user = form_obj.save()
            user.set_password(user.password)
            user.save()
            # 自动登录
            obj = auth.authenticate(request, **form_obj.cleaned_data)
            auth.login(request, obj)
            return redirect(reverse('index:index'))

    return render(request, 'index/reg.html', {'form_obj': form_obj})


def logout(request):
    auth.logout(request)
    return redirect(reverse('index:index'))
