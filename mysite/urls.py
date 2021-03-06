"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from accounts.views import *
from managing.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('manager/', manager_screen, name='manager'),
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('employee/', postVacancyEmployee, name='employeePost'),
    path('employer/', postVacancyEmployer, name='employerPost'),
    re_path(r'uploads/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT, })
]
