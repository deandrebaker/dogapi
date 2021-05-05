from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=50)
    weight = models.PositiveSmallIntegerField()
    sex = models.BooleanField(choices=[(True, "M"), (False, "F")])
    date_of_birth = models.DateTimeField(auto_now_add=True)
    is_good = models.BooleanField()

    def __str__(self):
        return self.name
