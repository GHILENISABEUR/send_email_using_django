from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'./templates/index.html')


from django.shortcuts import render
from django.core.mail import send_mail
from .forms import UserForm

def send_email_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            # Sending email
            subject = 'Welcome to Our Platform!'
            message = f'Hi {name},\n\nThank you for signing up!'
            from_email = 'your_email@gmail.com'
            recipient_list = [email]

            send_mail(subject, message, from_email, recipient_list)

            return render(request, 'email_sent.html', {'name': name})
    else:
        form = UserForm()

    return render(request, 'user_form.html', {'form': form})
