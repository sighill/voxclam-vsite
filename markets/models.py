from django.db import models
from django.utils import timezone
from battle.models import Character
from random import randint

# IF A MODEL HAS A FEEDER, MODIFY THE FEEDER IF YOU MODIFY THE MODEL

# This class is supposed to be filled with fixed data in backend
# It'll be filled with all possible markets entries
# The displayed markets entries will be copied randomly from the table
# created with this class and copied in their respective markets
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
    # WIP
    '''def __publish__(nbEntries):
        # Copy random entries from the BP to their respective
        # displayed markets, <nbEntries> times
        
        # Initiating variables
        # Array containing the objects to be published
        entriesPending = []
        # The lucky number used to pick each entry
        randomPick = 0
        for i in range(nbEntries):
            randomPick = randint(0,)
            entriesPending.append()
        self.published_date = timezone.now()'''
            


# This class will generate active markets items, randomly picked 
# every game turn to populate the Opp market.
# Every object from this class will be available to the players
# through their interface : they'll be able to buy them.
# WIP : add a visibility system based on reputation and or other variables
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
    published_date = models.DateTimeField(blank=True, null=True)
    # Owner field, left blank until bought by character
    owner = models.ForeignKey(
              Character 
            , related_name='marketOppOwner' # To avoid clash and missing dependency
            , blank=True # Will be blank when not bought
            , null=True ) # noob failsafe lolilol
    # WIP market Opp view requirements
    # WIP we have to develop a "reputation engine"
    
    ### FUNCTIONS #####################
    def __str__(self):
        return self.Gid

# This class will generate active markets items, randomly picked 
# every game turn to populate the Con market.
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
    published_date = models.DateTimeField(blank=True, null=True)
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