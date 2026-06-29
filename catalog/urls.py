from django.urls import path

from . import views

urlpatterns = [
    path("health/", views.health, name="health"),
    path("stores/", views.stores, name="stores"),
    path("products/", views.products, name="products"),
    path("catalog/", views.catalog, name="catalog"),
]
