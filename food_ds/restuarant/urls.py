from django.urls import path
from .import views

urlpatterns = [
    path('',views.home_view),
    path('login/',views.login_view),
    path('logout/',views.logout_view),
    path('register/',views.register_view),
    path('restaurant/', views.restaurant_view, name='restaurantinfo'),
    path('restaurant/editdetails/', views.restaurant_edit_details_view, name='restauranteditdetails'),
    path('restaurant/updateitems/', views.restaurant_update_items_view, name='restaurantupdateitems'),
]
