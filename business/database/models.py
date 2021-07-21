# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils.translation import gettext_lazy as _

class People(models.Model):
    number = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    
    def __str__(self):
    	return (self.name + ' ' + self.lastname)

    class Meta:
        managed = False
        db_table = 'people'


class Timing(models.Model):
    mykey = models.AutoField(primary_key=True)
    number = models.ForeignKey(People, models.DO_NOTHING, db_column='number')
    entry = models.DateTimeField()
    leaving = models.DateTimeField()
    
    def __str__(self):
    	return (str(self.entry) + ' ' + str(self.leaving))

    class Meta:
        managed = False
        db_table = 'timing'
        
class Exhibition(models.Model):
    start = models.DateField(_("Start"))
    end = models.DateField(_("End"), blank=True, null=True)
    opening = models.TimeField(_("Opening every day"))
    closing = models.TimeField(_("Closing every day"))

    class Meta:
        verbose_name = _("Exhibition")
        verbose_name_plural = _("Exhibitions")

    def __str__(self):
        return self.title
