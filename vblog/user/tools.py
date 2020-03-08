import random
from django.core.mail import send_mail
from .models import EmailValidLog


def generate_code():
    length = 4
    code = ''
    for i in range(length):
        code += str(random.randint(0,9))

    return code


def send_code_mail(title,who,code):
    msg = "您的注册验证码为：%s" % code
    rs = send_mail(title, msg, '420720973@qq.com', [who], fail_silently=False)
    code_log = EmailValidLog.objects.create(email=who, code=code)
    code_log.save()
