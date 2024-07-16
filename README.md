# Emailer
This Email Sender application allows users to send emails with an optional attachment. It is built using Django for the backend and Bootstrap for the frontend to ensure a responsive and user-friendly interface.


## Features
. Send emails by specifying recipient, subject, and message.
. Attach files to emails.
. Responsive design using Bootstrap.

## Requirements
.Python 3.6+
.Django 3.0+
.Bootstrap 4.5+

## Installation
1.git clone projecct

2 Configure email settings:

Edit settings.py to add your email details:

```
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your_smtp_server'
EMAIL_PORT = your_smtp_port
EMAIL_USE_TLS = True # or False, depending on your email provider
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_email_password'

```
