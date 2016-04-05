# ---------------------------------------------------------------------
# App markets
# Mise à disposition d'entrées de marché pour les joueurs.
# Les joueurs achètent des entrées pour en tirer une plus-value.
# Je profite de cette app pour tester la méthode d'écriture PEP 0008
# https://www.python.org/dev/peps/pep-0008/
# ---------------------------------------------------------------------

# Import des libairies
from random import randint
from datetime import datetime
# Import des modèles django
from markets.models import *
from geo.models import Stradi

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
    rand_pick = randint(0,len(alea_set)-1)

    # L'objet dont le gid est à la position rand_pick 
    #   dans l'array alea_set est extrait
    chosen_object = class_name.objects.get(pk=alea_set[rand_pick])
    
    # TEST ZONE
    #print('alea_set : {}'.format(alea_set))
    #print('rand_pick : {}'.format(rand_pick))
    #print('alea_set[rand_pick] : {}'.format(alea_set[rand_pick]))
    
    return chosen_object

#######################################################################
# MarketEntryBuilder est la fonction permettant de créer un objet
# d'entrée de marché.
#######################################################################
def MarketEntryBuilder(entry_picked):

    if entry_picked.category == 1:
        new_entry = MarketOpp(  title = entry_picked.title,
                                corpus = entry_picked.corpus,
                                price_flo = entry_picked.price_flo,
                                price_hon = entry_picked.price_hon,
                                price_fav = entry_picked.price_fav,
                                price_con = entry_picked.price_con,
                                reputation = entry_picked.reputation,
                                published_date = datetime.now()
                                )
    else:
        new_entry = MarketCon(  title = entry_picked.title,
                                corpus = entry_picked.corpus,
                                price_flo = entry_picked.price_flo,
                                price_hon = entry_picked.price_hon,
                                price_fav = entry_picked.price_fav,
                                price_con = entry_picked.price_con,
                                reputation = entry_picked.reputation,
                                published_date = datetime.now()
                                )

    # Insertion de l'objet dans le marché correspondant
    new_entry.save()


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
     # Déclaration de variables

    # Boucle de remplissage, tourne tant que refill_quantity > 0
    while refill_quantity > 0:
        # Choix d'une entrée MarketBlu au hasard
        entry_picked = RandomPicker(MarketBlu)

        # Appel de la fonction de construction de la nouvelle entrée
        MarketEntryBuilder(entry_picked)

        # Decrementer la quantité à remplir
        refill_quantity -= 1


#######################################################################
# WIP ZONE
# Je stocke ici tous les snippets intéressant, soit dépréciés soit
# en cours de création
#######################################################################

''' 
05/04/2016 11:45 utilisation d'un dictionnaire pour différencier
catégorie de marché dans lequel le nouvel objet va être inséré
#######################################################################
# MarketEntryBuilder est la fonction permettant de créer un objet
# d'entrée de marché.
#######################################################################
def MarketEntryBuilder(entry_picked):
    # Définition du dico des catégories de marché possibles
    market_dict = { '1':MarketOpp() , '2':MarketCon() }
    new_entry = market_dict.(entry_picked.category)
    # Remplissage d'une entrée de marché Opp on Con, en fonction
    # de la catégorie de l'objet 'entry_picked'
    new_entry = (  entry_picked.title = title,
                                entry_picked.corpus = corpus,
                                entry_picked.price_flo = price_flo,
                                entry_picked.price_hon = price_hon,
                                entry_picked.price_fav = price_fav,
                                entry_picked.price_con = price_con,
                                entry_picked.reputation = reputation
                                )
'''