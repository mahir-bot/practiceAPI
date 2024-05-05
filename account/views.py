from django.shortcuts import redirect, render
from django.contrib import messages
from account.models import User

# Create your views here.


def user_register(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        street_address = request.POST.get('street_address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        postal_code = request.POST.get('postal_code')
        country = request.POST.get('country')

        # Create the user object
        User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            street_address=street_address,
            city=city,
            state=state,
            postal_code=postal_code,
            country=country
        )
        messages.success(request, 'Account created successfully')
        return redirect('home')
    else:
        return render(request, 'account/register.html')
