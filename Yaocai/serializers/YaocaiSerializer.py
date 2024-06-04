from rest_framework import serializers
from Yaocai.models import Yaocai


class YaocaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yaocai
        fields = '__all__'
