from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Customer
from django.contrib import messages


def index(request):
    customers = Customer.objects.all().values()
    template = loader.get_template('index.html/')
    context = {
        'customers': customers,
    }
    return HttpResponse(template.render(context, request))
    # return render(request, 'index.html/')


def signin(request):
    return render(request, 'auth/signin.html/')


def add_customer(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        contact_email = request.POST['contact_email']
        acquired_on = request.POST['acquired_on']
        customer_status = request.POST['customer_status']

        new_customer = Customer(
            company_name=company_name,
            first_name=first_name,
            last_name=last_name,
            contact_email=contact_email,
            acquired_on=acquired_on,
            customer_status=customer_status,
        )
        new_customer.save()
        messages.success(request, 'Customer added successfully!')
        return redirect('index')
    return render(request, 'add_customer.html')


def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)

    if request.method == 'POST':
        # Retrieve data from the request
        company_name = request.POST['company_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        contact_email = request.POST['contact_email']
        acquired_on = request.POST['acquired_on']
        customer_status = request.POST['customer_status']

        # Update the customer object with the new data
        customer.company_name = company_name
        customer.first_name = first_name
        customer.last_name = last_name
        customer.contact_email = contact_email
        customer.acquired_on = acquired_on
        customer.customer_status = customer_status

        # Save the updated customer object
        customer.save()

        messages.success(request, 'Customer updated successfully!')

        # Redirect to the index page or any other appropriate URL
        return redirect('index')

    # If it's a GET request, render the edit_customer.html template with the existing customer data
    return render(request, 'edit_customer.html', {'customer': customer})


def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        customer.delete()
        messages.success(request, 'Customer deleted successfully!')
        return redirect('index')
    return render(request, 'index.html')
