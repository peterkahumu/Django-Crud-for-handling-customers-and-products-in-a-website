from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Product, Customer

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'Ecommerce/product_list.html', context)


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, "Ecommerce/product_details.html", context)

def addp(request):
    return render(request, "Ecommerce/add_product.html", {}) # load the form the user will use to update the products

def add_product(request):
    name = request.POST['name']
    description = request.POST['description']
    price = request.POST['price']
    availability = request.POST['availability']

    product = Product(name = name, description = description, price = price, availability = availability)
    product.save()
    messages.success(request, "Product added successfully.")

    return redirect('../../') # add the product and redirect the user to the product list

def updatep(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        "product": product
    }

    return render(request, "Ecommerce/update_product.html", context) # load the form to update a product

def update_product(request, pk):
    name = request.POST['name']
    description = request.POST['description']
    price = request.POST['price']
    availability = request.POST['availability']

    product = get_object_or_404(Product, pk = pk)
    product.name = name
    product.description = description
    product.price = price
    product.availability = availability
    product.save()
    messages.success(request, "Product updated successfully.")
    return redirect("../") # update the product and redirect the user to the product list

def delete_product(request, pk):
    product = get_object_or_404(Product, pk = pk)
    product.delete()
    messages.success(request, "Product deleted successfully.") # delete a product from the database.

    return redirect('../')

def customer_list(request):
    customers = Customer.objects.all().values()
    return render(request, 'Ecommerce/customer_list.html', {'customers': customers}) # display all the customerd in the database.

def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'Ecommerce/customer_detail.html', {'customer': customer}) # display the details of a specific customer

def update(request, pk):
    customer = get_object_or_404(Customer, pk = pk)
    context = {
        'customer': customer,
    }
    return render(request, "Ecommerce/update_customer.html", context) # load the form to update the customer details.

def update_customer(request, pk):
    # pick the updated data from the form.
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    phone = request.POST['phone']
    address = request.POST['address']

    # get the customer from the database and update the details.
    customer = get_object_or_404(Customer, pk=pk)
    customer.first_name = first_name
    customer.last_name = last_name
    customer.email = email
    customer.phone = phone
    customer.address = address

    customer.save()
    messages.success(request, 'Customer Updated Successfully')
    
    return redirect('../..') # update the customer details and redirect the user to the customer list page.
    

def delete_customer(request, pk):
    customer = get_object_or_404(Customer, pk = pk)
    customer.delete()
    messages.success(request, "Customer Deleted successfully.")

    return redirect('../') # delete all the details for a given customer.


def add(request):
    return render(request, 'Ecommerce/add_customer.html', {}) # load the form to add a new customer

def add_customer(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    phone = request.POST['phone']
    address = request.POST['address']

    customer = Customer(first_name = first_name, last_name = last_name, email = email, phone = phone, address = address)
    customer.save()
    messages.success(request, "Customer added successfully")

    return redirect('../..') # add a new customer to the database.


