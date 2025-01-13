from django.http import HttpResponse
from service.models import Service
from portfolio.models import Portfolio
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from datetime import datetime


from django.shortcuts import render

def home(request):

    services = Service.objects.all()

    portfolios = Portfolio.objects.all()

    experience = datetime.now().year - 2018

    return render(request, 'pub_templates/index.html', {'services':services, 'portfolios':portfolios, 'experience':experience})


def contact_us_email(request):

    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        service = request.POST.get("service", "")
        subject = "Contact with us."
        message = request.POST.get("message", "")
        # recipient = request.POST.get("email", "recipient@example.com")
        html_content = render_to_string("pub_templates/send_mail.html", {
            "name": name,
            "email": email,
            "service": service,
            "subject": subject,
            "message": message,
        })
        from_email = "contact@techpartit.net"
        recipient_list = ["recipient@example.com"]


        email = EmailMessage(subject, html_content, from_email, ["gkpritom@gmail.com"])
        email.content_subtype = "html"  # Set the email content type to HTML
        email.send()
        return HttpResponse("Email sent successfully!")
    return HttpResponse("Submit the form to send an email.")


