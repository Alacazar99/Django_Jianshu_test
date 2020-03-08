from django.db import models
from django.utils import timezone

from user.models import  User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100,null=False)
    create_user = models.ForeignKey(User,on_delete = models.CASCADE, null=True)

    class Meta:
        db_table = "tb_category"
        verbose_name = "类别"
        verbose_name_plural = verbose_name


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    read_times = models.IntegerField(default=0)
    zan_times = models.IntegerField(default=0)
    cai_times = models.IntegerField(default=0)
    create_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'tb_article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name
