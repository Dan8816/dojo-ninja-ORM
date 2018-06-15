# Inside models.py
from __future__ import unicode_literals
from django.db import models
# Create your models here.
class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length = 2)
    desc = models.TextField()

    def __repr__(self):
        return "<dojo: {} | {} {} {}>".format(self.id, self.name, self.city, self.state)

class Ninjas(models.Model):
    dojo = models.ForeignKey(Dojos, related_name="has_ninjas")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __repr__(self):
        return "<ninja: {} | {} {}>".format(self.id, self.dojo, self.first_name, self.last_name)
