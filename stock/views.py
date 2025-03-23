from django.urls import reverse_lazy
from django.views import generic
from stock.models import Product
from stock.forms import ProductForm

class ProductListView(generic.ListView):
    model = Product
    template_name = "product/list.html"

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "product/detail.html"

class ProductCreateView(generic.CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product/create.html"
    success_url = reverse_lazy("product-list")

class ProductUpdateView(generic.UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "product/update.html"
    success_url = reverse_lazy("product-list")

class ProductDeleteView(generic.DeleteView):
    model = Product
    template_name = "product/delete.html"
    success_url = reverse_lazy("product-list")