from django.db import models
from django.contrib.auth.models import AbstractUser


class Author(AbstractUser):
    Author_ID = models.IntegerField(primary_key=True, null=False)
    Organization = models.TextField(null=True)


class Archetypes(models.Model):
    Archetypes_ID = models.TextField(primary_key=True, null=False)
    Class = models.TextField(null=False)
    Archetypes_Description = models.TextField(null=True)


class School(models.Model):
    School_ID = models.TextField(primary_key=True, null=False)
    School_Description = models.TextField(null=True)


class Item_Type(models.Model):
    Item_Type_ID = models.TextField(primary_key=True, null=False)
    Item_Type_Description = models.TextField(null=True)


class Size(models.Model):
    Size_ID = models.TextField(primary_key=True, null=False)
    Size_Description = models.TextField(null=True)


class Species(models.Model):
    Species_ID = models.TextField(primary_key=True, null=False)
    Species_Description = models.TextField(null=True)


class Worldview(models.Model):
    Worldview_ID = models.TextField(primary_key=True, null=False)
    Worldview_Description = models.TextField(null=True)


class Armor(models.Model):
    Armor_ID = models.TextField(primary_key=True, null=False)
    Armor_Description = models.TextField(null=True)
    Armor_Class = models.IntegerField(null=True)


class Language(models.Model):
    Language_ID = models.TextField(primary_key=True, null=False)
    Language_Description = models.TextField(null=True)


class Habitat(models.Model):
    Habitat_ID = models.TextField(primary_key=True, null=False)
    Habitat_Description = models.TextField(null=True)


class Spells(models.Model):
    Spell_ID = models.TextField(primary_key=True, null=False)
    Spell_Author = models.ForeignKey('Author', on_delete=models.DO_NOTHING, to_field='Author_ID')
    Spell_Level = models.IntegerField(null=False)
    School = models.ForeignKey('School', models.DO_NOTHING, to_field='School_ID')
    Time_Application = models.TextField(null=True)
    Distance = models.TextField(null=True)
    Duration = models.TextField(null=True)
    Components = models.TextField(null=False)
    Archetypes = models.ForeignKey('Archetypes', models.DO_NOTHING, to_field='Archetypes_ID')
    Description = models.TextField(null=True)

    def __str__(self):
        field_values = self.__dict__
        return str({field: value for field, value in field_values.items() if not field.startswith('_')})


class Items(models.Model):
    Item_ID = models.TextField(primary_key=True, null=False)
    Item_Author = models.ForeignKey('Author', on_delete=models.DO_NOTHING, to_field='Author_ID')
    Item_Type = models.ForeignKey('Item_Type', on_delete=models.DO_NOTHING, to_field='Item_Type_ID')
    Item_Subtype = models.TextField(null=True)
    Item_Rarity = models.TextField(null=False)
    Item_Setting = models.TextField(null=True)
    Item_Price = models.TextField(null=True)
    Item_Description = models.TextField(null=True)

    def __str__(self):
        field_values = self.__dict__
        return str({field: value for field, value in field_values.items() if not field.startswith('_')})



class Bestiary(models.Model):
    Bestiary_ID = models.TextField(primary_key=True, null=False)
    Bestiary_Author = models.ForeignKey('Author', on_delete=models.DO_NOTHING, to_field='Author_ID')
    Size_ID = models.ForeignKey('Size', on_delete=models.DO_NOTHING, to_field='Size_ID')
    Species_ID = models.ForeignKey('Species', on_delete=models.DO_NOTHING, to_field='Species_ID')
    Worldview_ID = models.ForeignKey('Worldview', on_delete=models.DO_NOTHING, to_field='Worldview_ID')
    Armor_ID = models.ForeignKey('Armor', on_delete=models.DO_NOTHING, to_field='Armor_ID')
    Hits = models.IntegerField(null=False)
    Speed = models.TextField(null=False)
    Language_ID = models.ForeignKey('Language', on_delete=models.DO_NOTHING, to_field='Language_ID')
    Characteristics = models.TextField(null=False)
    Resistance_Damage = models.TextField(null=True)
    Immunity_Damage = models.TextField(null=True)
    Skills = models.TextField(null=True)
    Habitat_ID = models.ForeignKey('Habitat', on_delete=models.DO_NOTHING, to_field='Habitat_ID')
    Danger = models.IntegerField(null=False)
    Description = models.TextField(null=True)

    def __str__(self):
        field_values = self.__dict__
        return str({field: value for field, value in field_values.items() if not field.startswith('_')})
