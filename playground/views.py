from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    return 10

# Create your views here.
def say_hello(request):
    x = calculate()
    return render(request, 'hello.html')