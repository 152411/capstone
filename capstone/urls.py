"""capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#from django.urls import path
from django.conf.urls import include, url
from django.conf import settings
from django.shortcuts import redirect
from django.views.generic import RedirectView

def root(request):
    return redirect('project:post_list')

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', root, name='root'),

    url(r'^project/', include('project.urls', namespace='project')),
    url(r'^assignment/', include('assignment.urls', namespace='assignment')),
    url(r'^accounts/', include('accounts.urls')),
]


if settings.DEBUG:
     import debug_toolbar
     urlpatterns += [
     url(r'^__debug__/', include(debug_toolbar.urls)),
     ]