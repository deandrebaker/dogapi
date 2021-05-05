from django.db import models
from dogs.models import Dog


class Toy(models.Model):
    name = models.CharField(max_length=50)
    weight = models.PositiveSmallIntegerField()
    fun_rating = models.PositiveSmallIntegerField(choices=list(map(lambda i: (i, str(i)), range(1, 6))))
    dog = models.ForeignKey(to=Dog, on_delete=models.CASCADE, related_name="toys")

    def __str__(self):
        return self.name
