from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
   path("home", views.home, name="home"),
   path("writer",views.writer, name="writer"),
   path("blog/category", views.category, name="category"),
   path("blog/category/delete",views.category_delete, name="category_delete"),
   path("blog/article",views.article,name="article"),
   path("blog/fileupload",views.fileupload, name="fileupload")
]