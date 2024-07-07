from django.urls import path
from . import views

app_name = 'Ecommerce'

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_details, name='product_details'), # product details
    path('products/addp/', views.addp, name = 'load product add form'), # load the form to add a new product.
    path('products/addp/add_product/', views.add_product, name = 'add product'),
    path('products/update/<int:pk>', views.updatep, name = 'load update form'),
    path('products/update_product/<int:pk>', views.update_product, name = 'update product'),
    path('products/delete_product/<int:pk>', views.delete_product, name = 'Delete product'),
    
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customers/add/', views.add, name = 'load customer add form'),
    path('customers/add/add_customer/', views.add_customer, name = 'add_ customer'),
    path('customers/update/<int:pk>/', views.update, name = 'Update'),
    path('customers/update/update_customer/<int:pk>', views.update_customer, name = 'update customer'),
    path('customers/delete_customer/<int:pk>', views.delete_customer, name = 'delete_customer'),

    # products

]

