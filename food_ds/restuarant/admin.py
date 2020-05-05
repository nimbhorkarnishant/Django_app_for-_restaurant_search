from django.contrib import admin
from .models import Restaurant
from .models import Item
from .models import Element
from .models import ItemReview


# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Element)
admin.site.register(ItemReview)
