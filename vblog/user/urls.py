from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
   path("login", views.login, name="login"),
   path("register", views.register, name="register"),
   path("sendcode",views.sendcode,name="sendcode"),
   path("validemail",views.validemail, name="validemail")
]