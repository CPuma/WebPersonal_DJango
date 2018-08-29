from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(requests):
    projects = Project.objects.all() 

     ## Genera error por que Project.objects se genera cuando se inicia el sistema y pylint no lo sabe 
     ## pip install pylint-django   
     #  VSCODE - Setting ->(edit) 
     #                        python.linting.pylintArgs": [ "--errors-only","--load-plugins","pylint_django"]
    
    
    return render(requests, 'portfolio/portfolio.html', {'projects':projects})

