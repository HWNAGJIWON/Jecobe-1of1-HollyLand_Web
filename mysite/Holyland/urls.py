from django.contrib import admin
from django.urls import path
from main.views import index, mypage,signin,signup,detail,detail2

urlpatterns = [
    path('detail2/',detail2),
    path('detail/',detail),
    path('signin/',signin),
    path('signup/',signup),
    path('mypage/',mypage),
    path('admin/', admin.site.urls),
    path('', index),
]
