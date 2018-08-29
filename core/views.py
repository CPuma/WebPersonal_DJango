from django.shortcuts import render, HttpResponse

# Create your views here.
def home(requests):
    return render(requests, 'core/home.html')

def about(requests):
    return render(requests, 'core/about.html') 



def contact(requests):
    return render(requests, 'core/contact.html')