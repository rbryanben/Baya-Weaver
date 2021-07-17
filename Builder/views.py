from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView

from .forms import ThemeForm


# Builder
def builder_(request, project):
    # GET method return builder application
    if (request.method == "GET"):
        context = {
            "project": project
        }
        return render(request, 'Builder/Builder.html', context)


# theme upload
def theme_upload(request):
    if request.method == 'POST':
        form = ThemeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('Builder/test.html')
    context = {
        "form": form
    }
    return render(request, 'theme', context)
