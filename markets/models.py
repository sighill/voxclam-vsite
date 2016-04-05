from django.db import models
from django.utils import timezone
from battle.models import Character
from random import randint

# IF A MODEL HAS A FEEDER, MODIFY THE FEEDER IF YOU MODIFY THE MODEL

#######################################################################
# This class is supposed to be filled with fixed data in backend
# It'll be filled with all possible markets entries
# The displayed markets entries will be copied randomly from the table
# created with this class and copied in their respective markets
#######################################################################
class MarketBlu(models.Model):
    ### ATTRIBUTES #####################
    # market blueprint unique id
    gid = models.AutoField(primary_key=True)
    # market Blueprint category either Con or Opp
    category = models.IntegerField(default=1) # Default is Opp
    # market Blueprint title
    title = models.CharField(max_length=255)
    # market Blueprint text
    corpus = models.CharField(max_length=1200)
    # market BP prices
    price_flo = models.IntegerField(default=0) # florins
    price_com = models.IntegerField(default=0) # points commerce
    price_hon = models.IntegerField(default=0) # points honor
    price_fav = models.IntegerField(default=0) # points faveur divine
    price_con = models.IntegerField(default=0) # points contrats
    # Timestamp
    created_date = models.DateTimeField(default=timezone.now)
    # market BP view requirements
    reputation = models.IntegerField(default=-2)
    # WIP we have to develop a "reputation engine"
    
    ### FUNCTIONS #####################
    def __str__(self):
        return self.title

#######################################################################
# This class will generate active markets items, randomly picked 
# every game turn to populate the Opp market.
# Every object from this class will be available to the players
# through their interface : they'll be able to buy them.
#######################################################################
class MarketOpp(models.Model):
    ### ATTRIBUTES #####################
    # market Opp unique id
    gid = models.AutoField(primary_key=True)
    # market Opp title
    title = models.CharField(max_length=255)
    # market Opp text
    corpus = models.CharField(max_length=1200)
    # market Opp prices
    price_flo = models.IntegerField(default=0) # florins
    price_com = models.IntegerField(default=0) # points commerce
    price_hon = models.IntegerField(default=0) # points honor
    price_fav = models.IntegerField(default=0) # points faveur divine
    price_con = models.IntegerField(default=0) # points contrats
    # Timestamp
    published_date = models.DateTimeField(null=True)
    reputation = models.IntegerField(default=-2)
    # Owner field, left blank until bought by character
    owner = models.ForeignKey(
              Character 
            , related_name='marketOppOwner' # To avoid clashes
            , blank=True # Will be blank when not bought
            , null=True ) # noob failsafe lolilol
    # WIP market Opp view requirements
    # WIP we have to develop a "reputation engine"
    
    ### FUNCTIONS #####################
    def __str__(self):
        return self.Gid

    #def __init__(self):
    #    self.title = title
    #    self.corpus = corpus
    #    self.price_flo = price_flo
    #    self.price_hon = price_hon
    #    self.price_fav = price_fav
    #    self.price_con = price_con
    #    self.reputation = reputation
    #    # self.published_date = published_date

#######################################################################
# This class will generate active markets items, randomly picked 
# every game turn to populate the Con market.
#######################################################################
class MarketCon(models.Model):
    ### ATTRIBUTES #####################
    # market Con unique id
    gid  = models.AutoField(primary_key=True)
    # market Con title
    title = models.CharField(max_length=255)
    # market Con text
    corpus = models.CharField(max_length=1200)
    # market Con prices
    price_flo = models.IntegerField(default=0) # florins
    price_com = models.IntegerField(default=0) # points commerce
    price_hon = models.IntegerField(default=0) # points honor
    price_fav = models.IntegerField(default=0) # points faveur divine
    price_con = models.IntegerField(default=0) # points contrats
    # Timestamp
    published_date = models.DateTimeField(null=True)
    reputation = models.IntegerField(default=-2)
    # Owner field, left blank until bought by character
    owner = models.ForeignKey(
              Character 
            , related_name='marketConOwner' # To avoid clash and missing dependency
            , blank=True # Will be blank when not bought
            , null=True ) # noob failsafe lolilol
    # market Con view requirements
    # WIP we have to develop a "reputation engine"
    
    ### FUNCTIONS #####################
    def __str__(self):
        return self.Gid

    #def __init__(self):
    #    self.title = title
    #    self.corpus = corpus
    #    self.price_flo = price_flo
    #    self.price_hon = price_hon
    #    self.price_fav = price_fav
    #    self.price_con = price_con
    #    self.reputation = reputation
    #    # self.published_date = published_date