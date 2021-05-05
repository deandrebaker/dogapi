from rest_framework import serializers
from dogs.models import Dog
from toys.serializers import ToySerializer


class DogSerializer(serializers.ModelSerializer):
    toys = ToySerializer(many=True, read_only=True)

    class Meta:
        model = Dog
        fields = '__all__'
