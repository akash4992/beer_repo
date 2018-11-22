"""beerproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from beerapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.show),
    url(r'^beer/',views.beerlist),
    url(r'^add/',views.addbeer),
    url(r'^action/',views.action),
    url(r'^delete/(?P<id>\d+)/$', views.deletebeer),
    url(r'^update/(?P<id>\d+)/$', views.beerupdate),
    url(r'^signup/',views.Signup),
    url(r'login/',views.Login),
    url(r'^logout',views.Logout),
    url(r'^search/',views.search)

    

]
