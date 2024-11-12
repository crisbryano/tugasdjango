from django.shortcuts import render, redirect
from subscribeapp.models import Customer
from subscribeapp.forms import NewSubs

# Create your views here.

def index(request):
    return render(request, 'subscribeapp/index.html')

def customers(request):
    customer_list = Customer.objects.order_by('first_name')
    customer_dict = {'customers': customer_list}
    return render(request, 'subscribeapp/customers.html', context=customer_dict)

def subscribe(request):
    form = NewSubs()

    if request.method == 'POST':
        form = NewSubs(request.POST)
        if form.is_valid():  # Corrected to check if the form is valid
            # Handle form submission here, e.g., save to the database
            form.save()  # Assuming you want to save the new subscription
            return redirect('customers')  # Redirect to the customers page after form submission
        else:
            print("Error: Form is invalid.")  # Log the error if form is invalid
    else:
        print("No POST data received.")  # Log message for GET request

    return render(request, 'subscribeapp/subscribe.html', {'form': form})
