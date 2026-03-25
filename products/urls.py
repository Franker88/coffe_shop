from django.urls import path
from products import views

urlpatterns = [
    path('add/', views.ProductFormView.as_view(), name='add_product'),
    path('list/', views.ProductListView.as_view(), name='product_list'),
]