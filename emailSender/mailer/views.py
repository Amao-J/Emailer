
from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import EmailForm
from django.conf import settings

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            recipients = form.cleaned_data['recipient'].split(',')
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            attachment = request.FILES.get('attachment')

            email = EmailMessage(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [recipient.strip() for recipient in recipients],
            )

            if attachment:
                email.attach(attachment.name, attachment.read(), attachment.content_type)

            try:
                email.send()
                return render(request, 'Sender/success.html')
            except Exception as e:
                print(e)
                return render(request, 'Sender/error.html')
    else:
        form = EmailForm()

    return render(request, 'Sender/send_email.html', {'form': form})