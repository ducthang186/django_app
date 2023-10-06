from django.urls import re_path
from appFive import views

app_name = 'appFive'

urlpatterns = [
    re_path(r'^register/$',views.register,name = 'register'),
    re_path(r'^user_login/$',views.user_login,name = 'user_login'),

]







