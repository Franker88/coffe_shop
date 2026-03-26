from django.urls import reverse_lazy
from django.views import generic

from rest_framework.views import APIView
from rest_framework.response import Response

from products.forms import ProductForm
from products.models import Product

from .serializers import ProductSerializer

class ProductFormView(generic.FormView):
    template_name = 'products/product_form.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

    def form_valid(self, form:ProductForm):
        form.save()
        return super().form_valid(form)

class ProductListView(generic.base.TemplateView):
    template_name = 'products/product_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_list'] = Product.objects.all()
        return context


class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
