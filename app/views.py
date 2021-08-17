from django.shortcuts import redirect, render
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def home(request):
    context = {
        "projects": Project.objects.all()[::-1]
    }
    return render(request, 'index.html', context)

def about(request):

    context = {
        "photo": Profile.objects.all()
    }
    return render(request, 'about.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        sender = request.POST.get('email')
        subject = request.POST.get('subject')
        message = f"hello my name is {name} \n {request.POST.get('message')}"
        recipients = ['joseph4jubilant@gmail.com']
        try:
            send_mail(subject, message, sender, recipients, fail_silently=True)
        except BadHeaderError:
            messages.warning(request, 'sorry there was an error and i didn\'nt receive your message')
            return redirect('contact')

        messages.success(request, 'Thanks🙌🙌, i just receive your message')
        return redirect('contact')

    elif request.method == 'GET':
        return render(request, 'contact.html')





############# error pages
def not_found_view(request, exception):
    return render(request, '404.html', status=404)


def not_500_found_view(request):
    return render(request, '500.html', status=500)


