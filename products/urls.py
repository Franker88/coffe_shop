from django.urls import path
from products import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('add/', views.ProductFormView.as_view(), name='add_product'),
    path('api/', views.ProductListAPI.as_view(), name='product_list_api')
]