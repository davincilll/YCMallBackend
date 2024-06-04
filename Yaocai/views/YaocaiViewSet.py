from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from Yaocai.models import Yaocai
from Yaocai.serializers import YaocaiSerializer


class YaocaiViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Yaocai.objects.all()
    serializer_class = YaocaiSerializer
    filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Yaocai.objects.all()
        categoryType = self.request.query_params.get('categoryType')
        if categoryType is not None:
            queryset = queryset.filter(categoryType=categoryType)
        return queryset
