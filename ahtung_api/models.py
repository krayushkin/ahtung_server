from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, unique=True)
    group = models.ForeignKey('Group')
    registration_id = models.CharField(max_length=100, unique=True)
    def __unicode__(self):
	    return u"{0} | {1} | {2}".format(self.name, self.registration_id, self.group.pk)

class Group(models.Model):
    group_id = models.CharField(max_length=100, unique=True)
    def __unicode__(self):
        return self.group_id

class Signal(models.Model):
    signal_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100, unique=True)
    def __unicode__(self):
        return self.name

class EnabledSignal(models.Model):
    group = models.ForeignKey('Group')
    signal = models.ForeignKey('Signal')
    def __unicode__(self):
        return "{0} | {1}".format(self.group.pk, self.signal.pk)


# Create your models here.
