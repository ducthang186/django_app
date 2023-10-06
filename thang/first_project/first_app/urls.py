from django.urls import re_path
from first_app import views
urlpatterns = [
    re_path(r'^$',views.index1,name = 'index1'),
    re_path(r'^$',views.form_name_view,name = 'form_name_view'),
    # re_path(r'^users/',views.get_user,name = 'get_user'),

]







