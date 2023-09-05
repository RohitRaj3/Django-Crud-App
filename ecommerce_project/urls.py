
from django.urls import path
from ecommerce_project import views

urlpatterns = [
    path('', views.registration,name="registration"),
    path('about', views.about,name="about"),
    path('insert', views.insertData,name="insertData"),
    path('update/<id>', views.updateData,name="updateData"),
    path('delete/<id>', views.deleteData,name="deleteData")
    # path('login', views.insertData,name="loginData")

]