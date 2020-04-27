from django.conf.urls import url
from . import views
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    url(r'^accounts/profile$', views.home, name='home'),
    url(r'^login/$', LoginView.as_view(template_name='api/login.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='api/logout.html'), name='logout'),
    url(r'^register/$', views.register, name='register'),

]
