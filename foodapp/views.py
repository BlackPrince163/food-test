from django.db.models import Prefetch
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from foodapp.models import FoodCategory, Food
from foodapp.serializers import FoodListSerializer


class FoodCategoryView(viewsets.ViewSet):
    serializer_class = FoodListSerializer

    def list(self, request):
        queryset = (
            FoodCategory
            .objects
            .prefetch_related(
                Prefetch(
                    'food',
                    queryset=Food.objects.prefetch_related('additional').filter(is_publish=True).order_by("internal_code")))
            .order_by('id'))

        serializer = FoodListSerializer(queryset, many=True)
        return Response(serializer.data)
