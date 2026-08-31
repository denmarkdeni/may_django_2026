
from django.urls import path
from bot import views

urlpatterns = [
    path('' , views.home , name="home"),
    path('about/',views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('show/' , views.show_data, name="show_data "),
    path('add/numbers/', views.add_numbers, name="add_two_nums"),
    path('employee/form/' , views.employee_form , name="employee_form"),
    path('employee/list/' , views.employee_list , name="employee_list"),
    path('employee/<int:emp_id>/' , views.employee_details , name="employee_details"),
    path('employee/delete/<int:pk>/', views.employee_delete , name="employee_delete"),
]