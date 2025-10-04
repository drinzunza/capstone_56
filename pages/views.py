from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

# Create your views here.


def home_view(request):
    return render(request, "pages/home.html")


def about_view(request):
    return render(request, "pages/about.html")


def contact_view(request):
    if request.method == "POST":
        # send email
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        message_body = f"This is an email from your page\n Name: {name}\n Email: {email}\n Message: {message}"

        send_mail(
            "Email from your page",
            message_body,
            email,
            ['sinzunza@sdgku.edu'] # <- your email (the email will be send to this address)
        )

        form = ContactForm(request.POST)
        return render(request, "pages/contact.html", {'form': form, 'sent':True})

    form = ContactForm()
    return render(request, "pages/contact.html", {'form': form})
