
from django.urls import path
from bot import views

urlpatterns = [
    path('' , views.home , name="home"),
    path('about/',views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('show/' , views.show_data, name="show_data "),
    path('add/numbers/', views.add_numbers, name="add_two_nums"),
    path('employee/form/' , views.employee_form , name="employee_form"),
    path('employee/query/' , views.query_employee , name="query_employee"),
    path('employee/list/' , views.employee_list , name="employee_list"),
    path('employee/<int:emp_id>/' , views.employee_details , name="employee_details"),
    path('employee/delete/<int:pk>/', views.employee_delete , name="employee_delete"),
    path('student/form/', views.student_form , name="student_form"),
    path('template/view/', views.RoboticView.as_view() , name="template_view"),
    path('products/',views.ProductListView.as_view(), name="products"),
    path('product/create/',views.ProductCreateView.as_view(), name="product_create"),
    path('products/<int:pk>/',views.ProductDetailView.as_view(), name="product_detail"),
    path('product/update/<int:pk>/',views.ProductUpdateView.as_view(), name="product_update"),
    path('product/delete/<int:pk>/',views.ProductDeleteView.as_view(), name="product_delete"),
    path('sign/in/', views.sign_in , name="sign_in"),
    path('sign/up/', views.sign_up , name="sign_up"),

    # api endpoints
    path('api/info/',views.sample_view),
    path('api/employees/',views.employee_info),
    path('api/employees/<int:id>/',views.employee_data),
    path('api/employees/create/',views.create_employee),
] 