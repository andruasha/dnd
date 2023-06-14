from django.db import models


class Summary(models.Model):
    name = models.CharField(max_length=128, blank=False)
    path = models.CharField(max_length=256, blank=False)
    user = models.IntegerField(null = False, blank = False, default=0)

    def __str__(self):
        return self.name