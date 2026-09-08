from django.shortcuts import render, HttpResponse, redirect
from bot.models import Student, Employee, Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
    
def home(request):
    # return HttpResponse("THIS IS THE HOME")
    # Student.objects.create(
    #     name = "Ravi",
    #     age = 23,
    #     email = "ravi@gmail.com",
    #     dob = "2001-8-12",
    #     fees = 20000
    # )
    # print("student created")

    return render(request, "home.html")
# task - models
# html form employees 
# name , username , password , email , dob , terms 
# when submit , data should store in db

def about(request):
    return HttpResponse("THIS IS THE ABOUT PAGE")
def contact(request):
    return render(request , "contact.html")
def show_data(request):
    context = {
        "planet":"earth",
        "family":"solar system",
        "types":{
            "animals":["cat","dog","cow"],
            "plants":["neem","coconut","palm"]
        }
    }
    location="chennai"
    return render(request, "show.html",{"location":location})
    
# in home.html , create a tag 
# to connect home , about , contact page
# students.html , view , url
# add students link in home.html
# location = "chennai"
# dict students = [
#     {
#         "name":"ashok","age":20, "course":"python"
#     },    
#     {
#         "name":"vasu","age":21, "course":"java"
#     },    
#     {
#         "name":"ganesh","age":22, "course":"python"
#     },    
# ]
    
def add_numbers(request):
    print(request.POST) 
    total = 0
    if request.method == "POST":
        a = request.POST.get("num1")
        b = request.POST.get("num2")
        total = int(a) + int(b)
    return render(request , "add_two_nums.html",{"answer":total})
    
def employee_form(request):
    message = ""
    if request.method == "POST":
        Employee.objects.create(
            name = request.POST.get("e_name"),
            username = request.POST.get("u_name"),
            password = request.POST.get("password"),
            salary = request.POST.get("salary"),
            dob = request.POST.get("dob"),
            email = request.POST.get("email"),
            terms = request.POST.get("terms") == "on",
            profile = request.FILES.get("profile")
        )
        print(request.FILES)
        message="employee data created"
    return render(request, "employee/form.html",{"message":message})    

def employee_list(request):
    data = Employee.objects.all()
    return render(request , "employee/list.html",{"employees":data})

def employee_details(request, emp_id):
    employee = Employee.objects.get(id=emp_id)
    if request.method == "POST":
        employee.name = request.POST.get("e_name")
        employee.email = request.POST.get("email")
        employee.salary = request.POST.get("salary")
        employee.username = request.POST.get("u_name")
        employee.password = request.POST.get("password")
        employee.dob = request.POST.get("dob")
        employee.terms = request.POST.get("terms") == "on"
        employee.save()
        return redirect("employee_list")
    return render(request, "employee/update_form.html",{"employee":employee})
    
def employee_delete(request, pk):
    emp = Employee.objects.get(id=pk)
    emp.delete()
    messages.success(request, "Employee Deleted")
    return redirect("employee_list")
    
# Task 
# Products -> Products Section 
# Product create Form 
# name , catagory 
#(fruits, vegetables , groceries , cerials, medicines , clothes) 
# price , quantity , manufactured_date, expiry_date 
# is_registered , manufactured_place , GST %.
# products menu
# product card - edit , delete
    
# queryset 
    
# Model.objects.create()
# Model.objects.delete()
# Model.objects.get(field = value)
# Model.objects.all()
# Model.objects.filter(field = value)
# Model.objects.exclude(field = value)

from django.db.models import  Avg , Max ,Min , Count , Sum

def query_employee(request):
    keyword = request.GET.get("search") or ""
    # employees = Employee.objects.all()
    # employees = Employee.objects.get(id=10)
    # employees = Employee.objects.filter(id=10)
    # employees = Employee.objects.filter(terms=True)
    # employees = Employee.objects.filter(terms=True, salary=20000)
    # employees = Employee.objects.filter(salary__gt=50000)
    # employees = Employee.objects.filter(salary__lte=50000)
    # employees = Employee.objects.filter(name__istartswith="A")
    # employees = Employee.objects.filter(username__iendswith="3")
    # employees = Employee.objects.filter(role="admin",dob__gt="1995-01-01")
    # employees = Employee.objects.filter(role__in=["hr","manager"])
    # employees = Employee.objects.all().order_by("name")
    # employees = Employee.objects.all().order_by("-dob")
    # employees = Employee.objects.exclude(role="employee")
    # employees = Employee.objects.filter(role="employee",salary__gt=100000)
    employees = Employee.objects.filter(name__icontains=keyword)
    count = employees.count()
    print(employees.exists())
    print(Employee.objects.aggregate(total_salary =Sum("salary")))
    print(Employee.objects.aggregate(max_salary =Max("salary")))
    print(Employee.objects.aggregate(average_salary =Avg("salary")))
    return render(request , "employee/query_list.html", {"employees":employees , "count":count , "key":keyword})

from .forms import StudentForm

def student_form(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            print("student created")
    return render(request, "student_form.html",{"form":form} )

# CLASS BASED VIEWS

# template , detail ,list
# CREATE , UPDATE , DELETE

from django.views.generic import TemplateView , DetailView , ListView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from .models import Product
from django.urls import reverse_lazy

class RoboticView(TemplateView):
    template_name = "cbv/template.html"

class ProductListView(ListView):
    template_name = "cbv/product_list.html"
    context_object_name = "products"
    model = Product
    fields = "__all__"

class ProductCreateView(CreateView):
    template_name = "cbv/product_create.html"
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("products")

class ProductDetailView(DetailView):
    template_name = "cbv/product_detail.html"
    model = Product
    fields = "__all__"
    context_object_name = "product"

class ProductUpdateView(UpdateView):
    template_name = "cbv/product_update.html"
    model = Product
    fields = "__all__"
    success_url = reverse_lazy("products")

class ProductDeleteView(DeleteView):
    template_name = "cbv/product_delete.html"
    model = Product
    success_url = reverse_lazy("products")

# authentication vs authorisation 
# checking whether you are a user or not.
# checking user's permissions to allow.

# register - stores new user credentials
# login - checks if credentials stored in database

# auth_user 
# first_name , last_name , username , password
# last_joined , first_joined , is_superuser , 
# is_staff , email

# register page  , create credentials
# username , password , email 
# login page , username , password 
# if correct -> login successful
# else - invalid credentials
# authenticate , login , logout 

def sign_up(request):
    if request.method == "POST":
        u = User.objects.create_user(
            username = request.POST.get("username"),
            password = request.POST.get("password"),
            email = request.POST.get("email")
        )
        Profile.objects.create(
            user = u,
            role = request.POST.get("role")
        )
        print("user created")
        return redirect("sign_in")
    return render(request , "auth/sign_up.html")

def sign_in(request):
    if request.method == "POST":
        usr = request.POST.get("username")
        pwd = request.POST.get("password")
        u = authenticate(username = usr , password = pwd)
        if u:
            login(request, u)
            print("user loggedin successfully")
            print(u.username , u.profile.role)
        else:
            print("user not found")
    return render(request, "auth/sign_in.html")