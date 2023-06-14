from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):
    Author_ID = models.IntegerField(primary_key=True, null=False)
    Name = models.TextField(null=False)
    Last_Name = models.TextField(null=False)
    Organization = models.TextField(null=True)


class Archetypes(models.Model):
    Archetypes_ID = models.TextField(primary_key=True, null=False)
    Class = models.TextField(null=False)
    Archetypes_Description = models.TextField(null=True)


class school(models.Model):
    School_ID = models.TextField(primary_key=True, null=False)
    School_Description = models.TextField(null=True)


class Item_Type(models.Model):
    Item_Type_ID = models.TextField(primary_key=True, null=False)
    Item_Type_Description = models.TextField(null=True)



class Spells(models.Model):
    Spell_ID = models.TextField(primary_key=True, null=False)
    Spell_Author = models.IntegerField()
