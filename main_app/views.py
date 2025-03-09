from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def index_page(request):
    
    if request.method == 'POST':
       first_name = request.POST.get('first_name')
       
       message = request.POST.get('message')
       last_name = request.POST.get('last_name')
       emaill = request.POST.get('emaill')
       
       send_mail('Contact Form',
        f"first name:- {first_name}\n last name:- {last_name}\n message:- {message}\n email:- {emaill}",
        settings.EMAIL_HOST_USER,
        ['kunaladwani1456@gmail.com'], 
        fail_silently=False)
    
    if request.method == 'POST':
       email2 = request.POST.get('email2')
       
       send_mail('Contact Form',
        f"email:- {email2}",
        settings.EMAIL_HOST_USER,
        ['kunaladwani1456@gmail.com'], 
        fail_silently=False)
    

    return render(request,"index.html")