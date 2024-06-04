from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from Yaocai.models import Yaocai
from Yaocai.serializers import YaocaiSerializer


class YaocaiViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Yaocai.objects.all()
    serializer_class = YaocaiSerializer
