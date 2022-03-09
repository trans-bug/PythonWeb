"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    
"""

from django.contrib import admin
from django.urls import re_path,path,include

from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

from boards import views

from dj_store import views as storeviews

#path这一行是一个python元组：第一个参数是模式匹配字符串，第二个参数是调用的试图函数，第三个参数是
#python将视图函数作为一个对象传递，而不是调用，这使得函数可以项变量一样传递

urlpatterns = [
    #这一部分是账户登录的url
    re_path(r'^$', views.BoardListView.as_view(), name='home'),
    
    re_path(r'^accounts/',include('accounts.urls')),
    
    #这一部分是帖子相关的url
    re_path(r'^boards/',include('boards.urls')),
    
    
    #这一部分是商城相关的url
    re_path(r'^store_homepage/$', storeviews.storehome.store_homepage,name="store_homepage"),
    
    #这是时间板块的url
    re_path(r'^current_datetime/$', views.current_datetime,name="current_datetime"),
]



'''
松耦合,决定URL返回哪个视图函数和实现这个视图函数是在两个不同的地方,这使得修改一个地方不影响其他地方

'''