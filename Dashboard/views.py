from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
import json

@csrf_exempt
def login_(request):
    #GET method return the login page
    if (request.method == "GET"):
        return render(request,'Dashboard/Authentication/Login.html')
    
    #POST method attempt login
    if (request.method == "POST"):
        username = requestGetJSONValue(request,'username')
        password = requestGetJSONValue(request,"password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("200")
        else:
            return HttpResponse("Invalid Credentials")



def requestGetJSONValue(request,key):
    received_json = json.loads(request.body)
    return received_json[key]
