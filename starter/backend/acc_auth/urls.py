"""_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from . import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import TemplateView

app_name = 'accounts'

urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path('delete-account/', views.delete_account, name="delete-account"),
    path('settings/', views.settings, name="settings"),
    path('completed/', views.completed, name="completed"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('dashboard/', TemplateView.as_view(template_name="accounts/dashboard.html"), name = 'dashboard'),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("images/favicon.ico"))),

    ]
    