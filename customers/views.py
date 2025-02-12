from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Customer



@login_required
def customer_list(request):
    """
    View to display a list of all customer.
    Supports HTML and JSON responses.
    """
    customer = Customer.objects.all()
    if request.headers.get('Content-Type') == 'application/json':
        customer_data = [
            {"name": customer.name,
             "vat_id": customer.vat_id,
             "city": customer.city,
             "country": customer.country,
             }
            for customer in customer
        ]
        return JsonResponse(customer_data, safe=False)
    return render(request,
                  'customer/customer_list.html',
                  {'customer': customer})




@login_required
def customer_detail(request, pk):
    """
    View to display details of a single customer.
    Supports HTML and JSON responses.
    """
    customer = get_object_or_404(Customer, pk=pk)
    if request.headers.get('Content-Type') == 'application/json':
        customer_data = {
            "name": customer.name,
            "vat_id": customer.vat_id,
            "city": customer.city,
            "country": customer.country,
        }
        return JsonResponse(customer_data)
    return render(request, 'customer/customer_detail.html', {'customer': customer})


@login_required
def customer_create(request):
    """
    View to create a new customer.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        vat_id = request.POST.get('vat_id')
        city = request.POST.get('city')
        country = request.POST.get("country")


        if name and vat_id and city and country:
            customer = customer.objects.create(name=name, vat_id=vat_id , city=city , country=country)
            return redirect('customer_list')
        return render(request, 'customer/customer_create_form.html', {'error': 'All fields are required.'})

    return render(request, 'customer/customer_create_form.html')


@login_required
def customer_update(request, pk):
    """
    View to update an existing customer.
    """
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.name = request.POST.get('name', customer.name)
        customer.vat_id = request.POST.get('vat_id', customer.vat_id)
        customer.city = request.POST.get('city', customer.city)
        customer.country = request.POST.get("country", customer.country)
        customer.save()
        return redirect('customer_list')

    return render(request, 'customer/customer_edit_form.html', {'customer': customer})
