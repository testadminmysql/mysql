from django.conf.urls import url 
from django.urls import include, path

from myapp import views 
 
urlpatterns = [ 
    url(r'^api/employees$', views.employee),
    url(r'^api/employee_list$', views.employee_list),
    url(r'^api/employee_add$', views.employee_add),
    path('',views.display,name='display'),
    ]