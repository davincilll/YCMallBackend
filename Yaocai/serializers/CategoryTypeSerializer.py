from rest_framework import serializers

from Yaocai.models import CategoryType


class CategoryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryType
        fields = '__all__'
