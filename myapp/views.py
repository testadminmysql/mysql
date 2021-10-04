from django.shortcuts import render

from django.http.response import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from myapp.models import employees
from myapp.serializers import EmployeeSerializer
from rest_framework.decorators import api_view
def display(request):
    st=employees.objects.all() # Collect all records from table 
    print(st)
    return render(request,'display.html',{'st':st})

@api_view(['GET', 'POST', 'DELETE'])
def employee(request):
    if request.method == 'GET':
        Employees = employees.objects.all()
        
        employeeid = request.GET.get('id', None)
        print(employeeid)
        if employeeid is not None:
            print("2")
            Employe = Employees.filter(id__icontains=employeeid)
            print(Employe)
        
        
        employee_serializer = EmployeeSerializer(Employe, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
 

@api_view(['GET'])
def employee_list(request):
    if request.method == 'GET':
        Employees = employees.objects.all()
        
        
        employee_serializer = EmployeeSerializer(Employees, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
        
@api_view(['POST'])
def employee_add(request):
    if request.method == 'POST':
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')
        email = request.GET.get('email')
        phone_number = request.GET.get('phone_number')
        hire_date = request.GET.get('hire_date')
        print(first_name,last_name,email,phone_number,hire_date)
        employees.objects.create(first_name=first_name,last_name=last_name,email=email,phone_number=phone_number,hire_date=hire_date)

        
        
        return HttpResponse("Successfully Added") 

