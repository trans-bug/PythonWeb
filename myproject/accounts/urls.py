from django.urls import re_path
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    
    #注册相关
    re_path(r'^signup/$', accounts_views.signup, name='signup'),
    
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
   
    #这一部分是管理员的url
    re_path(r'admin/', admin.site.urls),
    
    
    #这一部分是密码相关的url
    re_path(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
            ),
            name='password_reset'),
    
    re_path(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    
    re_path(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    
    re_path(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
        name='password_change'),
    
    re_path(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
        name='password_change_done'),
]
