from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from stock.models import Product

class ProductListView(ListView):
    model = Product
    template_name = "product/list.html"

class ProductDetailView(DetailView):
    model = Product
    template_name = "product/detail.html"

class ProductCreateView(CreateView):
    model = Product
    fields = ["name", "description", "bar_code", "amount", "manufacturer_reference"]
    template_name = "product/create.html"
    success_url = reverse_lazy("product-list")

class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name", "description", "bar_code", "amount", "manufacturer_reference"]
    template_name = "product/update.html"
    success_url = reverse_lazy("product-list")

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product/delete.html"
    success_url = reverse_lazy("product-list")