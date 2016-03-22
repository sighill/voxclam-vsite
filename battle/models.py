from django.db import models

# Create your models here.

# Classe du joueur, point d'entrée physique dans le jeu
class Player(models.Model):
    # Player unique id
    playerGid = models.AutoField(primary_key=True)
    # Player name
    playerName = models.CharField(max_length=200)
    # Used to return the name of the iteration in admin panel
    def __str__(self):
        return self.playerName

# Classe personnage, que vont incarner les joueurs.
class Character(models.Model):
    # Character unique id
    characterGid = models.AutoField(primary_key=True)
    # name of the character
    characterName = models.CharField(max_length=200)
    # class of the character (noble, merchant, cleric)
    characterClassChoices = ( 
        ( 'Noble'    , 'Noble'    ) ,
        ( 'Merchant' , 'Merchant' ),
        ( 'Cleric'   , 'Cleric'   ))
    characterClass = models.CharField(
        max_length=200 ,
        choices = characterClassChoices ,
        default = 'Cleric')
    # Owner of the character : calls the primary key of a Player object
    characterOwner = models.ForeignKey(Player)
    # Used to return the name of the iteration in admin panel
    def __str__(self):
        return self.characterName

# Classe équipement, qui pourra être équipé par les groupes
class Equipment(models.Model):
    # Equipment unique id
    equipmentGid = models.AutoField(primary_key=True)
    # Equipment type
    equipmentTypeChoices = (
        ( 'Arme'    , 'Arme'    ) ,
        ( 'Armure'  , 'Armure'  ) ,
        ( 'Spécial' , 'Spécial' ) )
    equipmentType  = models.CharField(
        max_length = 200 ,
        choices    = equipmentTypeChoices ,
        default    = 'Arme')
    # name of the equipment
    equipmentName = models.CharField(max_length=200)
    # Owner of the equipment
    equipmentOwner = models.ForeignKey(Character)
    # group carrying the equipment
    # Group class is declared after this one so the class name is string
    # equipmentCarrier = models.ForeignKey('Group' , blank=True , null=True)
    # Which equipment is this, RH, LH or armor
    equipmentSlotChoices = (
        ( 'Main droite' , 'Main droite' ) ,
        ( 'Main gauche' , 'Main gauche' ) ,
        ( 'Armure'      , 'Armure'      ) )
    equipmentSlot  = (models.CharField(
        max_length = 200 ,
        choices    = equipmentSlotChoices ,
        default    = 'Main droite'))
    # equipment stat modifiers
    modPAC = models.IntegerField(default=0)
    modMOV = models.IntegerField(default=0)
    modINI = models.IntegerField(default=0)
    modSTR = models.IntegerField(default=0)
    modEVA = models.IntegerField(default=0)
    modDEF = models.IntegerField(default=0)
    modFAV = models.IntegerField(default=0)
    modMOR = models.IntegerField(default=0)
    modSPE = models.CharField(max_length = 200 , default=0)
    # Used to return the name of the iteration in admin panel
    def __str__(self):
        return self.equipmentName

# Classe groupe
class Group(models.Model):
    # Group unique id
    groupGid = models.AutoField(primary_key=True)
    # name of the group
    groupName = models.CharField(max_length=200)
    # Owner of the group
    groupOwner = models.ForeignKey(Character)
    # Group's healthy members
    groupMemberHealthy = models.IntegerField(default=30)
    # Group's injured members
    groupMemberInjured = models.IntegerField(default=0)
    # Group's dead members
    groupMemberDead = models.IntegerField(default=0)
    # group native stats
    groupPAC = models.IntegerField(default=6)
    groupMOV = models.IntegerField(default=2)
    groupINI = models.IntegerField(default=2)
    groupSTR = models.IntegerField(default=2)
    groupEVA = models.IntegerField(default=2)
    groupDEF = models.IntegerField(default=2)
    groupFAV = models.IntegerField(default=0)
    groupMOR = models.IntegerField(default=0)
    groupSPE = models.CharField(max_length=200 , default=0)
    # Equipment slots
    equiRH = models.ForeignKey(Equipment , related_name='equiRH')
    equiLH = models.ForeignKey(Equipment , related_name='equiLH')
    equiArmor = models.ForeignKey(Equipment, related_name='equiArmor')
    # Used to return the name of the iteration in admin panel
    def __str__(self):
        return self.groupName

