from django.db import models
from django.contrib.gis.db import models

#####################################################################
# Classe de quartiers de ville                                         
#####################################################################
class Sestieri(models.Model):
    # ATTRIBUTES ##########
    gid = models.AutoField(primary_key=True)
    # secondary id for gis workflow
    id = models.IntegerField(null = True)
    country = models.CharField(max_length=255)
    sestiere = models.CharField(max_length=255)
    commentary = models.CharField(null = True,
                                  max_length=1200)
    modified = models.DateTimeField(null = True)
    # geodjango specific
    geom = models.PolygonField()
    # METHODS #############
    def __str__(self):
        return str(self.gid)

class Ponti(models.Model):
    # ATTRIBUTES ##########
    gid = models.AutoField(primary_key=True)
    # secondary id for gis workflow
    id = models.IntegerField(null = True)
    country = models.CharField(max_length=255)
    pont = models.CharField(max_length=255)
    commentary = models.CharField(null = True,
                                  max_length=1200)
    modified = models.DateTimeField(null = True)
    # geodjango specific
    geom = models.LineStringField()
    # METHODS #############
    def __str__(self):
        return str(self.gid)
