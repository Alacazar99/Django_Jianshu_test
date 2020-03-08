from django.db import models
from django.utils import timezone
import hashlib


# Create your models here.
class User(models.Model):
    gender_choice = (
        (1, "男"),
        (0, "女")
    )
    user_name = models.CharField(verbose_name="用户名", unique=True, null= False, max_length=100)
    password = models.CharField(verbose_name="密码", null=False,max_length=200)
    gender = models.CharField(choices=gender_choice, max_length=2)
    email = models.EmailField(null=False, unique=True,max_length=100)
    tel = models.CharField(null=True, unique=True, max_length=20)
    create_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user_name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.password = hashlib.md5(self.password.encode("utf-8")).hexdigest()
        super().save()


class EmailValidLog(models.Model):
    email = models.EmailField(null=False, unique=False, max_length=100)
    code = models.CharField(max_length=10)
    send_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table= 'tb_email_valid_log'