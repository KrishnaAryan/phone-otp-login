
from django.contrib import admin
from django.urls import path,include, re_path
from .views import *

urlpatterns = [
    re_path('^validate_phone/',ValidatePhoneSendOTP.as_view()),
    re_path('^validate/',ValidateOTP.as_view()),
    re_path('^register/',Register.as_view()),
]
