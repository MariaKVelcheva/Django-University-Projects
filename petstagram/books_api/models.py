from django.db import models


class Book(models.Model):
    title = models.CharField(
        max_length=100,
    )

    pages = models.IntegerField(
        default=0,
    )

    description = models.TextField(
        default=""
    )

    author = models.CharField(
        max_length=100,
    )

