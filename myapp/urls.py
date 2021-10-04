from django.conf.urls import url 
from myapp import views 
 
urlpatterns = [ 
    url(r'^api/employees$', views.employee),
    url(r'^api/employee_list$', views.employee_list),
    url(r'^api/employee_add$', views.employee_add),
    ]