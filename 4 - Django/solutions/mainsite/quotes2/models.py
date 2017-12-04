from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Quote(models.Model):
    body = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.body + ' - ' + self.author.name

