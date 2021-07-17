from django.http.response import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from Dashboard.views import requestGetJSONValue
from django.views.decorators.csrf import csrf_exempt
from Dashboard.models import Project

#Builder 
def builder_(request,project):
    #GET method return builder application
    if (request.method == "GET"):
        context = {
            "project" : project
        }
        return render(request,'Builder/Builder.html',context)


@csrf_exempt
def create_project_(request):
    if (request.method == "POST"):
        #params
        name = requestGetJSONValue(request,'name')
        template = requestGetJSONValue(request,'template')
        user = request.user
        title = requestGetJSONValue(request,'title')
        
        #template to string 
        render_data = {
            "title" : title
        }
        new_template = render_to_string('Builder/Startup_Templates/gym_template.html',render_data)

        #store record
        new_project_record = Project()
        new_project_record.create(request.user,name)

        #new file
        html_file = open('client_data/'+new_project_record.file_id,'w+')
        html_file.write(new_template)
        html_file.close()

        #return success
        return HttpResponse("200")


@csrf_exempt
def get_project_template(request,id):
    #template 
    template = open(f'client_data/{id}','r+').read()
    return HttpResponse(template)

