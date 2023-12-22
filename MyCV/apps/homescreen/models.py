from django.db import models
from django.db.models import CharField, TextField, DateTimeField, DateField, ImageField


class Project(models.Model):
    title = CharField(max_length=60)
    pic = ImageField(upload_to='')
    description = TextField()
    short_description = CharField(max_length=255)
    pubdate = DateTimeField()
    dist_date = DateField()

    def __str__(self):
        return self.title

