from django.urls import path

from orders.views import CreateOrderProductView, MyOrderView

urlpatterns = [
    path("order/", MyOrderView.as_view() ,name="order"),
    path("add_product/", CreateOrderProductView.as_view(), name="add_order")
]
