from django.urls import path
from .import views

urlpatterns =[
    path('search/', views.search_view,name='search'),
    path('restaurant/',views.search_restaurant_view, name='restaurant'),
    path('item/', views.item_view, name='item'),
    path('item/addreview/',views.item_review, name='item_review'),
]
