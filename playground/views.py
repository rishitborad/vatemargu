from django.shortcuts import render
from django.http import HttpResponse
from .models import airport_list
from .models import flight

def calculate():
    return 10

# Create your views here.
def say_hello(request):
    x = calculate()
    return render(request, 'hello.html')

def display(request):
    arp=airport_list.objects.all() # Collect all records from table 
    num_records = arp.count()  # Get the count of records
    return render(request,'display.html',{'arp':arp, 'num_records': num_records})