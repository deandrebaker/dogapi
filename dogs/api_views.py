from rest_framework.viewsets import ModelViewSet
from dogs.serializers import Dog, DogSerializer


class DogViewSet(ModelViewSet):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer
