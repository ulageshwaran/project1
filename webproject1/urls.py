from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("blog",views.blog),
    path("cart",views.cart),
    path("category",views.category),
    path("checkout",views.checkout),
    path("confirmation",views.confirmation),
    path("contact",views.contact),
    path("elements",views.elements),
    path("login",views.login),
    path("tracking",views.tracking),
    path("single-blog",views.single_blog),
    path("single-product",views.single_product),
]