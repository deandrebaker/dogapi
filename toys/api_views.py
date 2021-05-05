from rest_framework.viewsets import ModelViewSet
from toys.serializers import Toy, ToySerializer


class ToyViewSet(ModelViewSet):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
