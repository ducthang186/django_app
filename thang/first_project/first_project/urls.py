"""
URL configuration for first_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path, include
from first_app import views
from appFive import views as views1
urlpatterns = [
    path("admin/", admin.site.urls),
    re_path(r'^first_app/',include('first_app.urls')),
    # re_path(r'^$', views.index1,name='index1'),
    re_path(r'^homepage/', views.form_name_view,name='form_name_view'),
    re_path(r'^appFive/',include('appFive.urls')),
    re_path(r'^$',views1.index,name ='index'),
    re_path(r'^logout/',views1.user_logout,name ='logout'),
    re_path(r'^special/',views1.special,name ='special'),

]
