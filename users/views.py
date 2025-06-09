from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render
# Create your views here.
def homepage(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request,'about.html')
def loginpage(request):
    return render(request,'login.html')
def registerpage(request):
    return render(request,'register.html')