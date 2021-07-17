from django.http.response import HttpResponse
from django.shortcuts import render

#Builder 
def builder_(request,project):
    #GET method return builder application
    if (request.method == "GET"):
        context = {
            "project" : project
        }
        return render(request,'Builder/Builder.html',context)