from django.db import models
from django.contrib.gis.db import models as gismodels

#####################################################################
# Classe de quartiers 
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
    geom = gismodels.PolygonField()
    # METHODS #############
    def __str__(self):
        return str(self.gid)

#####################################################################
# Classe de ponts
#####################################################################
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
    geom = gismodels.LineStringField()
    # METHODS #############
    def __str__(self):
        return str(self.gid)
        
#####################################################################
# Classe de rues
#####################################################################
class Stradi(models.Model):
    # ATTRIBUTES ##########
    gid = models.AutoField(primary_key=True)
    # secondary id for gis workflow
    id = models.IntegerField(null = True)
    country = models.CharField(max_length=255)
    via = models.CharField(max_length=255)
    commentary = models.CharField(null = True,
                                  max_length=1200)
    modified = models.DateTimeField(null = True)
    # geodjango specific
    geom = gismodels.LineStringField()
    # METHODS #############
    def __str__(self):
        return str(self.gid)
