from django.db.models import Prefetch
from rest_framework import viewsets

from foodapp.models import FoodCategory, Food
from foodapp.serializers import FoodListSerializer


class FoodCategoryViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.filter(food__is_publish=True)
    serializer_class = FoodListSerializer

    def get_queryset(self):
        queryset = FoodCategory.objects.filter(food__is_publish=True).prefetch_related(
            Prefetch("food", queryset=Food.objects.filter(is_publish=True))
        ).distinct()
        return queryset


