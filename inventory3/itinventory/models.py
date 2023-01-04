from django.db import models

# Create models here.
class Rooms(models.Model):
  roomname = models.CharField(max_length=255)
  anzahlplaetze = models.IntegerField(default=None)
class Pcs(models.Model):
    modell = models.CharField(max_length=255)
    RAM = models.CharField(max_length=255)
    CPU = models.CharField(max_length=255)
    anzahlkerne = models.CharField(max_length=255)
    festplatte = models.CharField(max_length=255, null=True)
    serialnummer = models.CharField(max_length=50,default=None, null=True, blank=True)
    monitor1 = models.CharField(max_length=50,default=None, null=True, blank=True)
    monitor2 = models.CharField(max_length=50,default=None, null=True, blank=True)
    bemaerkung = models.CharField(max_length=300,default=None, null=True, blank=True)
    status = models.CharField(max_length=100,default=None, null=True, blank=True)
   
class Monitor(models.Model):
      schnittstelle = models.CharField(max_length=255)
      serialnummer = models.CharField(max_length=55,default=None, null=True, blank=True)
      bemaerkung = models.CharField(max_length=300,default=None, null=True, blank=True)
      status = models.CharField(max_length=100,default=None, null=True, blank=True)
      
class Platz(models.Model):
  bezeichnung = models.CharField(max_length=50, null=True)
  room = models.ForeignKey(Rooms,on_delete=callable,null=True,default=None, related_name='Room')
  pc = models.ForeignKey(Pcs,on_delete=models.CASCADE, default=1,null=True)
  monitor1 = models.ForeignKey(Monitor,on_delete=callable, related_name='Monitor1', default=1,null=True)
  monitor2 = models.ForeignKey(Monitor,on_delete=callable, related_name='Monitor2', default=1,null=True)
  bemaerkung = models.CharField(max_length=300,default=None, null=True, blank=True)
  tastatur = models.BooleanField(default=False,null=True)
  maus = models.BooleanField(default=False,null=True)
  