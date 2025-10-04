from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductsList.as_view(), name="products_list"),
    path("cart/", views.CartListView.as_view(), name="cart"),
    path("add_cart/<int:pk>/", views.AddToCartView.as_view(), name="add_cart"),
    path("remove_cart/<str:pk>/", views.RemoveFromCartView.as_view(), name="remove_cart"),
]
