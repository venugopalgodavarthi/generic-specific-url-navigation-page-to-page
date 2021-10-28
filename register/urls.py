from django.urls import path
from register import views
urlpatterns=[
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('home/<name>/',views.homepage,name="home"),
 
    ]