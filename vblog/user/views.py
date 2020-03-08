from django.shortcuts import render,redirect,reverse
from django.core.mail import send_mail
from django.http import HttpResponse
import hashlib
import json

from .forms import RegisterForm,LoginForm
from .tools import generate_code,send_code_mail
from .models import User
from .excep import MyBaseException



# Create your views here.
def login(request):
    if request.method == "POST":
        try:
            form = LoginForm(request.POST)
            if form.is_valid():
                user = User.objects.filter(user_name=request.POST['user_name'])
                if len(user) == 0:
                    raise MyBaseException(code=1001,msg="用户名或密码错误")
                exist_user = user[0]
                password = request.POST['password']
                encode_pwd = hashlib.md5(password.encode("utf-8")).hexdigest()
                if encode_pwd != exist_user.password:
                    raise MyBaseException(code=1001, msg="用户名或密码错误")
                # 将用户信息保存到session中
                request.session['user'] = exist_user.id
                return redirect(reverse('blog:home'))
            else:
                return render(request, 'login.html', {'form': form})
        except MyBaseException as e:
            # form.add_error("password", e.msg)
            return render(request, 'login.html', {'form': form,'error_msg': e.msg})
    else:
        form = LoginForm()
        return render(request, 'login.html',{'form':form})


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'register.html',{'form':form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        form.set_session_validcode(request.session['valid_code'])

        if form.is_valid():
           form.save()
           return HttpResponse("创建成功")
        else:
            return render(request, 'register.html', {'form': form})


def sendcode(request):
    try:
        email = request.POST['email']
        if not email:
            raise RuntimeError()
        # 生成验证码
        code = generate_code()
        # 将验证码存到session中
        request.session['valid_code'] = code
        # 发送邮件
        # message = "您的注册验证码为：%s" % code
        # print(email,":",message)
        # rs = send_mail("微博客验证码", message, '420720973@qq.com', [email], fail_silently=False)
        # print(rs)
        send_code_mail("微博客验证码", email, code)
        return HttpResponse("ok")
    except Exception as e:
        print(e)
        return  HttpResponse("fail")


def validemail(request):
    email = request.GET.get("email")
    if not email:
        return HttpResponse("fail")

    user = User.objects.filter(email=email)

    if len(user) > 0 :
        return HttpResponse("fail")
    else :
        return HttpResponse("ok")
