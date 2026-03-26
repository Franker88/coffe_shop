from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from orders.forms import OrderProductForm

from .models import Order, OrderProduct

class MyOrderView(LoginRequiredMixin,DetailView):
    template_name = "orders/order.html"
    model = Order
    context_object_name = 'order'

    def get_object(self, queryset = None):
        user = self.request.user
        return Order.objects.filter(user=user,is_active=True).first()
    
class CreateOrderProductView(CreateView):
    template_name = "orders/add_order.html"
    form_class = OrderProductForm
    success_url = reverse_lazy('order')
    
    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(
            is_active=True,
            user=self.request.user,
        )
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)
    