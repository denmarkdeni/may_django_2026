from django.shortcuts import render, HttpResponse, redirect
from bot.models import Student, Employee
from django.contrib import messages
    
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
    
