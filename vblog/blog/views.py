from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt
from .models import Category,Article
from user.models import User
import time
import os
import json
from .tools import  json_data
# Create your views here.

# 跳转到home页面
def home(request):
    return render(request,'home.html')


def writer(request):
    if request.method == "POST":
        pass
    else :
        user_id = request.session['user']
        category_list = Category.objects.filter(create_user_id=user_id).order_by('-id')
        return render(request, 'writer.html',{'category_list':category_list})


@csrf_exempt
def category(request):
    user_id = request.session['user']
    # 新建文集输入检验
    if request.method == "POST":
        category_name = request.POST.get("name")
        if not category_name:
            return HttpResponse("类别不能为空！")
        user = User.objects.get(pk=user_id)
        cate = Category(category_name = category_name, create_user = user)
        cate.save()
        return HttpResponse("ok")
    else:
        category_list = Category.objects.filter(create_user_id=user_id).order_by('-id')
        data = serializers.serialize("json",category_list)

        return HttpResponse(data, content_type='application/json;charset=utf-8')


#
@csrf_exempt
def category_delete(request):
    cate_id = request.POST['cate_id']
    if not cate_id:
        return HttpResponse("fail")

    Category.objects.filter(id=cate_id).delete()
    return HttpResponse("ok")


@csrf_exempt
def article(request):
    if request.method == 'POST':
        try:
            title = request.POST['blog_title']
            content = request.POST['blog_content']
            category_id = request.POST['category_id']

            article_id = request.POST.get("article_id", None)
            user_id = request.session['user']

            if (not title) or (not content) or (not category_id) :
                raise KeyError
            if not article_id:
                article_id = None

            article = Article(id=article_id,title=title,content=content,category_id=category_id,author_id=user_id)
            article.save()
            data = {
                'article_id':article.id
            }
            return json_data(data = data)

        except KeyError:

            data = {'msg': '参数不合法'}
            return json_data(code = 1001,data=data)
    else:
        pass

@csrf_exempt
def fileupload(request):
    file = request.FILES.get("upload",None)
    if file is None:
        return HttpResponse("文件上传失败！")
    else:
        base_dir = "./"

        upload_dir ="/static/upload_files"
        #自动生成文件名
        file_name = int(time.time() * 1000)

        pos = file.name.rindex(".")
        suffix = file.name[pos:]
        upload_file_name = upload_dir + str(file_name) + suffix
        # 上传文件
        with open(os.path.abspath(base_dir +upload_file_name), "wb+") as f:

            for chunk in file.chunks():
                f.write(chunk)

        # return HttpResponse(upload_file_name)
        resp = {
            'uploaded':1,
            'fileName':file.name,
            'url':upload_file_name,
        }
        return HttpResponse(json.dumps(resp,ensure_ascii=False))

