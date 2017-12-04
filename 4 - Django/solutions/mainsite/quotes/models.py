from django.db import models


class Quote(models.Model):
    body = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    def __str__(self):
        return self.body + ' - ' + self.author








