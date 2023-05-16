from django.shortcuts import render
from .serializers import EmployeeSerializers
from django.views.decorators.csrf import csrf_exempt
from .models import employee
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse,HttpResponse
# Create your views here.


@csrf_exempt
def login(request):
     if request.method=='POST':
        employee_data=JSONParser().parse(request)
        email=employee_data.get('email')
        password=employee_data.get('password')
        employees=employee.objects.get(email=email)
        if employees:
            if email==employees.email:
                if email==employees.email and password != employees.password:
                    return JsonResponse("Invalid Passworrd",safe=False)
                elif email==employees.email and password==employees.password:
                    return JsonResponse("LOgin Successful",safe=False)
        else:
            return JsonResponse("Invalid Credentials",safe=False)

@csrf_exempt
def register(request):
    if request.method=="POST":
        employee_data=JSONParser().parse(request)
        employee_serializer=EmployeeSerializers(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Employee added Successfully",safe=False)

@csrf_exempt

def profile(request,email):
    if request.method=="GET":
        employees=employee.objects.get(email=email)
        employeedata={
             'firstname':employees.firstname ,
             'lastname':employees.lastname,
             'email':employees.email,
             'mobno':employees.mobno
        }
        if employees:
            return JsonResponse(employeedata,safe=False)
        else:
            return JsonResponse("No Employee",safe=False)
        
 
