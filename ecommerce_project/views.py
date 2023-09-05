from django.shortcuts import render,redirect
from .models import Product
from django.contrib import messages

# Create your views here.
def registration(request):
    data=Product.objects.all()
    context= {"data":data}
    return render(request,"registration.html",context)

def insertData(request):
    
    if request.method=="POST":
        name = request.POST.get('name')
        # lname = request.POST.get('last')
        email=request.POST.get('email')
        password=request.POST.get('password')
        gender = request.POST.get('gender')
        print(name,email,password,gender)
        query=Product(name=name,email=email, password=password, gender=gender)
        query.save()
        messages.info(request,"Data Inserted Successfully")
        return redirect("/")
    return render(request,"registration.html")

def updateData(request,id):
    if request.method=="POST":
        name = request.POST.get('name')
        # lname = request.POST.get('last')
        email=request.POST.get('email')
        password=request.POST.get('password')
        gender = request.POST.get('gender')

        edit=Product.objects.get(id=id)
        edit.name=name
        edit.email=email
        edit.gender=gender
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("/")
    d=Product.objects.get(id=id)
    context= {"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=Product.objects.get(id=id)
    d.delete()
    messages.error(request,"Data Deleted Successfully")

    return redirect("/")

# def loginData(request):
#     if request.method=="POST":
        
#         Email=request.POST.get('email')
#         Password=request.POST.get('password')
#         print(Email,Password)

#     return render(request,"upload.html")

def about(request):
    return render(request,"about.html")