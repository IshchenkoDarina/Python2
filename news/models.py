from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=120)
    post = models.CharField()
    date = models.DateTimeField()
    objects = models.Manager()

    def __str__(self):
        return self.title
