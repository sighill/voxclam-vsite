# ---------------------------------------------------------------------
# App markets
# Mise à disposition d'entrées de marché pour les joueurs.
# Les joueurs achètent des entrées pour en tirer une plus-value.
# Je profite de cette app pour tester la méthode d'écriture PEP 0008
# https://www.python.org/dev/peps/pep-0008/
# ---------------------------------------------------------------------

# Import des libairies
from random import randint
# Import des modèles django
from markets.models import *

#######################################################################
# RandomPicker permet d'extraire un objet au hasard au sein 
#   d'une classe qui est entrée en paramètre. 
# WIP : Seule l'appli markets seul MarketBlu utilise cette fonction 
#   mais bon on fait du générique !
#######################################################################
def RandomPicker(class_name):
    # Remplissage d'un array avec les gid de chaque entrée de marché
    # Ce sera l'ensemble dans lequel l'aléa va être tiré
    alea_set = []
    for obj in class_name.objects.all():
        alea_set.append(obj.gid)
    # Tirage d'un nombre entre 0 et le nombre d'objets
    rand_pick = randint(0,len(alea_set))
    # L'objet dont le gid est à la position rand_pick 
    #   dans l'array alea_set est extrait
    chosen_object = class_name.objects.get(pk=alea_set[rand_pick])
    # TEST ZONE
    # print('alea_set : {}'.format(alea_set))
    # print('rand_pick : {}'.format(rand_pick))
    # print('alea_set[rand_pick] : {}'.format(alea_set[rand_pick]))
    return chosen_object

#######################################################################
# MarketPublisher permet :
# 1. De tirer des modèles d'entrée de marché, de les personnaliser 
#    avec des ressources géographiques ou de noms de PNJ / PJ 
#    pour en faire des entrées uniques disponibles à l'achat.
# 2. De retirer des entrées de marché périmées qui auront subsisté 
#    deux tours de jeu complets (publié tour 1, retiré avant le tour 3)
# Cette fonction est appelée chaque tour de jeu pour gérer les marchés.
#######################################################################
def MarketPublisher(refill_quantity):
    
    

# To resolve the 
#def MarketResolver(entry_gid , character_gid):
    # WIP
#   return