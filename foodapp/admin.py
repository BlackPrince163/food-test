from django.contrib import admin

from foodapp.models import FoodCategory, Food

admin.site.register(FoodCategory)
admin.site.register(Food)
