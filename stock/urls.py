from django.urls import path
from stock.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path("", ProductListView.as_view(), name="product-list"),
    path("create/", ProductCreateView.as_view(), name="product-create"),
    path("<slug:pk>/", ProductDetailView.as_view(), name="product-detail"),
    path("<slug:pk>/update", ProductUpdateView.as_view(), name="product-update"),
    path("<slug:pk>/delete", ProductDeleteView.as_view(), name="product-delete")
]