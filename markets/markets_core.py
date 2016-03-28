# ---------------------------------------------------------------------
# App markets
# Mise à disposition d'entrées de marché pour les joueurs.
# Les joueurs achètent des entrées pour en tirer une plus-value.
# Les entrées MarketOpp vont donner un retour sur investissement
# ponctuel alors que MarketCon donne des retours réguliers
# comme des rentes.
# Je profite de cette app pour tester la méthode d'écriture PEP 0008
# https://www.python.org/dev/peps/pep-0008/
# ---------------------------------------------------------------------

from .models import *
from random import randint


# Fixed variables for test
refill_quantity = 1

# This function returns an object randomly picked within the 
# specified class
# Function RandomPick is designed to get the number of iterations
# in a class and within its range choose an iteration randomly

def RandomPicker(class_name):
	# Fill an array with all objects 
	# (IDs can be non continuous !)
	alea_boundaries = class_name.objects.all()
	# Choose a random number within the number of objects
	alea = randint(0,alea_boundaries.count())
	# Return the lucky one
	chosen_object = class_name.objects.get(pk=alea+1)
	return chosen_object


# Function made to publish entries to the displayed markets
# WIP : maybe we could def this encapsulated in class MarketBlu ?
def MarketPublisher(refill_quantity):
	
	

# To resolve the 
def MarketResolver(entry_gid , character_gid):
	# WIP
	return