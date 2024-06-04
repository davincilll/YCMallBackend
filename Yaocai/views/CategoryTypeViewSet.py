from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from Yaocai.models import CategoryType
from Yaocai.serializers import CategoryTypeSerializer


class CategoryTypeViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializer
    filter_backends = [sDjangoFilterBackend]
