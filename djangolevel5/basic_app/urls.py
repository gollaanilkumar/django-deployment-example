from django.urls import path
from .  import views


app_name="basic_app"

urlpatterns=[
    path('',views.index,name="index"),
    path('registration/',views.registration,name="registration"),
    path('login_user/',views.login_user,name="login_user"),
]