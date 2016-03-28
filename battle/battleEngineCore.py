
###############################################################################        
# Import des librairies nécessaires
###############################################################################
from random import randint
from math import floor , ceil , fabs
from .models import *

###############################################################################        
# Classe encapsulant la classe groupe et permettant de stocker les infos
# relatives au combat
###############################################################################
class GroupBattle:
    def __init__ ( self, group ):
        # Le groupe qui participe au combat
        self.group = group 

        # Les variables liées au combat
        self.won = False # Est-ce que ce groupe a gagné ?
        self.demoralized = False # Est-ce que ce groupe fuit ?
        self.bonusINI = False # Est-ce que ce groupe a le bonus d'initiative ?
        self.membersStartRound = 0  # Nombre de membre healthy au début du round
        self.residualDamage = 0  # Dégâts résiduels restant du round précédent

        # Caractéristiques du groupe (caracs de base + modif equipements)
        # TODO: qu'est-ce qui se passe si un groupe n'a pas d'equiLH par exemple ?
        self.caracPAC = group.groupPAC + group.equiRH.modPAC + group.equiLH.modPAC + group.equiArmor.modPAC
        self.caracMOV = group.groupMOV + group.equiRH.modMOV + group.equiLH.modMOV + group.equiArmor.modMOV
        self.caracINI = group.groupINI + group.equiRH.modINI + group.equiLH.modINI + group.equiArmor.modINI
        self.caracSTR = group.groupSTR + group.equiRH.modSTR + group.equiLH.modSTR + group.equiArmor.modSTR
        self.caracEVA = group.groupEVA + group.equiRH.modEVA + group.equiLH.modEVA + group.equiArmor.modEVA
        self.caracDEF = group.groupDEF + group.equiRH.modDEF + group.equiLH.modDEF + group.equiArmor.modDEF
        self.caracFAV = group.groupFAV + group.equiRH.modFAV + group.equiLH.modFAV + group.equiArmor.modFAV
        self.caracMOR = group.groupMOR + group.equiRH.modMOR + group.equiLH.modMOR + group.equiArmor.modMOR

        # Check des min / max
        # TODO: définir les min / max. Pour le moment je les met toutes entre 1 et 99
        if( self.caracPAC < 1 ):
            self.caracPAC = 1
        elif( self.caracPAC > 99 ):
            self.caracPAC = 99

        if( self.caracMOV < 1 ):
            self.caracMOV = 1
        elif( self.caracMOV > 99 ):
            self.caracMOV = 99

        if( self.caracINI < 1 ):
            self.caracINI = 1
        elif( self.caracINI > 99 ):
            self.caracINI = 99

        if( self.caracSTR < 1 ):
            self.caracSTR = 1
        elif( self.caracSTR > 99 ):
            self.caracSTR = 99

        if( self.caracEVA < 1 ):
            self.caracEVA = 1
        elif( self.caracEVA > 99 ):
            self.caracEVA = 99

        if( self.caracDEF < 1 ):
            self.caracDEF = 1
        elif( self.caracDEF > 99 ):
            self.caracDEF = 99

        if( self.caracFAV < 1 ):
            self.caracFAV = 1
        elif( self.caracFAV > 99 ):
            self.caracFAV = 99

        if( self.caracMOR < 1 ):
            self.caracMOR = 1
        elif( self.caracMOR > 99 ):
            self.caracMOR = 99

###############################################################################        
# Liste des variables globales utilisées par le Battle Engine
###############################################################################
        
# Le compte rendu de bataille
global battleLog

# Spécificités de la bataille
global numberOfRounds
global deathMatchMode

# Constantes utilisées pour l'équilibrage de la bataille
DEF_TO_PV_MULTIPLICATOR = 3

###############################################################################
# Cette fonction permet d'apporter du hasard dans le combat. 
# Elle renvoie un réel compris entre [number-margin %;number+margin %] 
# avec margin noté comme un pourcentage
###############################################################################
def delta( number, margin ):
    # vérifier que la marge est bien entre -100 et 100.
    if( margin < -100 ):
        margin = -100
    elif( margin > 100 ):
        margin = 100

    # appliquer le random
    deltaRandom = randint(-margin,margin)/100
    modificator = ceil(number * deltaRandom)
    randomizedValue = number + modificator

    # vérification des bornes
    if( randomizedValue < 0 ):
        randomizedValue = 0
    elif( randomizedValue > 100 ):
        randomizedValue = 100

    return randomizedValue

###############################################################################
# Cette function est le coeur du battle engine
# On lui fournit les deux groupes prêts à combattre
# et elle retourne le compte rendu du combat à afficher
###############################################################################
def performBattle( groupA, groupB ):    
    # On récupère les variables globales nécessaires...
    global battleLog
    global numberOfRounds
    global deathMatchMode

    #...et on les initialise
    battleLog = ""
    numberOfRounds = 0
    deathMatchMode = False

    # Détermination du nombre de rounds
    numberOfRounds = fabs( groupA.groupPAC - fabs( groupA.groupPAC - groupB.groupPAC ))

    # Annonce du mode de combat dans le log d'entête de bataille
    if deathMatchMode is False :
        deathMatchModeLog = 'Le combat se déroule dans l\'honneur, sans achever le groupe adverse'
    else:
        deathMatchModeLog = 'Le combat se déroule jusqu\'à la mort du groupe adverse !'
    

    # Création des objects stockant les groupes et les variables associées
    groupBattleA = GroupBattle( groupA )
    groupBattleB = GroupBattle( groupB )

    # Affichage d'infos utiles avant la bataille
    # TODO: gérer l'affichage des caracs dans la classe GroupBattle
    # Comme ça ce sera plus propre, on pourra tester l'existence des equip, et gérer les modifs +/- dans le log
    addLog( 'logNormal', 'Le groupe \"{}\" ({} , {} , {}) fait face au groupe \"{}\" ({} , {} , {} ). {}.'
                .format(groupA.groupName , groupA.groupMemberHealthy, groupA.groupMemberInjured , groupA.groupMemberDead , groupB.groupName , groupB.groupMemberHealthy , 
                    groupB.groupMemberInjured , groupB.groupMemberDead , deathMatchModeLog ))
    addLog( 'logNormal', 'Le groupe "{}" est équippé de {}, de {} et de {}'.format( groupA.groupName, groupA.equiRH, groupA.equiLH, groupA.equiArmor ))
    addLog( 'logNormal', 'Cela lui confère les caractéristiques suivantes: PAC={} ({}+{}+{}+{}), MOV={} ({}+{}+{}+{}), INI={} ({}+{}+{}+{}), STR={} ({}+{}+{}+{}), EVA={} ({}+{}+{}+{}), DEF={} ({}+{}+{}+{}), FAV={} ({}+{}+{}+{}), MOR={} ({}+{}+{}+{})'
        .format( groupBattleA.caracPAC, groupA.groupPAC, groupA.equiRH.modPAC, groupA.equiRH.modPAC, groupA.equiArmor.modPAC,
            groupBattleA.caracMOV, groupA.groupMOV, groupA.equiRH.modMOV, groupA.equiLH.modMOV, groupA.equiArmor.modMOV,
            groupBattleA.caracINI, groupA.groupINI, groupA.equiRH.modINI, groupA.equiLH.modINI, groupA.equiArmor.modINI,
            groupBattleA.caracSTR, groupA.groupSTR, groupA.equiRH.modSTR, groupA.equiLH.modSTR, groupA.equiArmor.modSTR,
            groupBattleA.caracEVA, groupA.groupEVA, groupA.equiRH.modEVA, groupA.equiLH.modEVA, groupA.equiArmor.modEVA,
            groupBattleA.caracDEF, groupA.groupDEF, groupA.equiRH.modDEF, groupA.equiLH.modDEF, groupA.equiArmor.modDEF,
            groupBattleA.caracFAV, groupA.groupFAV, groupA.equiRH.modFAV, groupA.equiLH.modFAV, groupA.equiArmor.modFAV,
            groupBattleA.caracMOR, groupA.groupMOR, groupA.equiRH.modMOR, groupA.equiLH.modMOR, groupA.equiArmor.modMOR ))
    addLog( 'logNormal', 'Le groupe "{}" est équippé de {}, de {} et de {}'.format( groupB.groupName, groupB.equiRH, groupB.equiLH, groupB.equiArmor ))
    addLog( 'logNormal', 'Cela lui confère les caractéristiques suivantes: PAC={} ({}+{}+{}+{}), MOV={} ({}+{}+{}+{}), INI={} ({}+{}+{}+{}), STR={} ({}+{}+{}+{}), EVA={} ({}+{}+{}+{}), DEF={} ({}+{}+{}+{}), FAV={} ({}+{}+{}+{}), MOR={} ({}+{}+{}+{})'
        .format( groupBattleA.caracPAC, groupA.groupPAC, groupA.equiRH.modPAC, groupA.equiRH.modPAC, groupA.equiArmor.modPAC,
            groupBattleB.caracMOV, groupB.groupMOV, groupB.equiRH.modMOV, groupB.equiLH.modMOV, groupB.equiArmor.modMOV,
            groupBattleB.caracINI, groupB.groupINI, groupB.equiRH.modINI, groupB.equiLH.modINI, groupB.equiArmor.modINI,
            groupBattleB.caracSTR, groupB.groupSTR, groupB.equiRH.modSTR, groupB.equiLH.modSTR, groupB.equiArmor.modSTR,
            groupBattleB.caracEVA, groupB.groupEVA, groupB.equiRH.modEVA, groupB.equiLH.modEVA, groupB.equiArmor.modEVA,
            groupBattleB.caracDEF, groupB.groupDEF, groupB.equiRH.modDEF, groupB.equiLH.modDEF, groupB.equiArmor.modDEF,
            groupBattleB.caracFAV, groupB.groupFAV, groupB.equiRH.modFAV, groupB.equiLH.modFAV, groupB.equiArmor.modFAV,
            groupBattleB.caracMOR, groupB.groupMOR, groupB.equiRH.modMOR, groupB.equiLH.modMOR, groupB.equiArmor.modMOR ))

    #########################################################
    #                 Boucle principale                     #
    #########################################################

    # La bataille dure tant que les PAC ne sont pas épuisés.
    # Le compteur de rounds est initialisé
    currentRound = 1
    while ( currentRound <= numberOfRounds ) and ( groupBattleA.won is False ) and (groupBattleB.won is False) and ( groupBattleA.demoralized is False) and ( groupBattleB.demoralized is False):
        # Ajout du nom du round au log
        addLog( 'logTitle' , 'Round {} :'.format(currentRound) )

        # On récupère les états des groupes en début de round
        groupBattleA.membersStartRound = groupBattleA.group.groupMemberHealthy
        groupBattleB.membersStartRound = groupBattleB.group.groupMemberHealthy
        
        # On lance le round de combat au corps à corps
        performBattleRoundH2H( groupBattleA, groupBattleB )

        # Fin du round, passage au round suivant
        currentRound += 1

    return battleLog

###############################################################################
# Cette exécute un round de combat entre deux groupes qui combattent au 
# corps à corps (hand-to-hand = H2H)
# C'est cette fonction qui sera appelé dans le cas d'une battaille entre
# deux armées
###############################################################################
def performBattleRoundH2H( groupBattleA, groupBattleB ):
    # On lance la 1e phase du round: uniquement lors du 1er round
    # TODO: dans le cadre d'une bataille entre deux armées, il faudra revoir
    # l'utilisation de l'initiative (puisque la notion de 1er round est différente)
    #if( currentRound == 1):
    #    addLog( 'logSubTitle' , 'Phase d\'initiative' )
    #    # Déterminer qui a le bonus d'initiative pour le 1er round
    #    phaseInitiative( groupBattleA, groupBattleB )
    #elif( currentRound == 2):
    #    # Sinon (à partir du round 2), plus de bonus d'initiative
    #    groupBattleA.bonusINI = False
    #    groupBattleB.bonusINI = False

    # On lance la 2e phase du round
    addLog( 'logSubTitle' , 'Phase de combat: "{}" attaque !'.format( groupBattleA.group.groupName ))
    phaseCombat( groupBattleA, groupBattleB )
    addLog( 'logSubTitle' , '"{}" riposte !'.format( groupBattleB.group.groupName ))
    phaseCombat( groupBattleB, groupBattleA )

    # TODO On lance la 3e phase du round
    # phaseMorale(groupA , groupB) 

    # On lance la 4e phase du round
    addLog( 'logSubTitle' , 'Phase de maintenance :')
    phaseMaintenance( groupBattleA, groupBattleB )

###############################################################################
# Phase d'initiative
###############################################################################
def phaseInitiative( groupBattleA, groupBattleB ):
    # On détermine qui a l'initiative, et donc le bonus de STR
    groupAINI = delta( groupBattleA.caracINI, 50 )
    groupBINI = delta( groupBattleB.caracINI, 50 )
    if( groupAINI > groupBINI ):
        addLog( 'logNormal', '{} obtient le bonus d\'initiative ! ({} vs {})'.format( groupBattleA.group.groupName , groupAINI, groupBINI ) )
        # Le groupe A à le bonus
        groupBattleA.bonusINI = True
    else :
        addLog( 'logNormal', '{} obtient le bonus d\'initiative ! ({} vs {})'.format( groupBattleB.group.groupName , groupBINI, groupAINI ) )
        # Le groupe B a le bonus
        groupBattleB.bonusINI = True
    #TODO: relancer si égalité

###############################################################################
# Cette fonction réalise l'attaque d'un groupe par un autre 
# Les imputs nécessaires sont (en plus des deux groupes):
# - le nombre de membres du groupe qui attaquent (membres valides en début de *
# round)
# - les dégâts résiduels du round précédent pour les défenseurs
###############################################################################
def phaseCombat( attacker, defender ):
    # Calcul des dégats infligés par l'attaquant :
    # 1) Chaque membre valide en début de round attaque avec sa force (+/- delta)
    sommeDegats = attacker.membersStartRound * ( delta( attacker.caracSTR, 50 ) )
    addLog( 'logNormal' , 'L\'attaquant attaque {} fois avec une force moyenne de {} pour un total de {} dégats'
                .format( attacker.membersStartRound, attacker.caracSTR, sommeDegats ) )
    
    # Calcul des dégats évités grâce à l'esquive 
    # 1) la carac EVA est un %age des dégats esquivés (+/- delta)
    percentEsquive = delta( defender.caracEVA, 50 )
    # 2) On applique ce %age aux dégats pour voir combien sont esquivés
    degatsEsquives =  floor( sommeDegats * percentEsquive / 100 )
    # 3) On soustrait les dégats esquivés à la somme des dégats
    sommeDegats -= degatsEsquives
    addLog( 'logNormal' , 'Le défenseur a en moyenne {} % de chances d\'esquiver. {} dégats sont esquivés. L\'attaquant inflige au final {} dégâts'
                .format( defender.caracEVA, degatsEsquives , sommeDegats ))
    
    # On inflige les dégats au défenseur, et on calcule les pertes. 
    # 1) On ajoute les dégats résiduels du tour précédent (si on les avait ajouté avant, le défenseur aurait pu les ré-ésquiver)
    sommeDegats += defender.residualDamage
    # 2) Chaque défenseur à DEF * X PV
    defPV = defender.caracDEF * DEF_TO_PV_MULTIPLICATOR
    # 3) Calcul du nombre de victimes
    victims = floor( sommeDegats / defPV )
    if( victims > defender.group.groupMemberHealthy ):
        victims = defender.group.groupMemberHealthy
    # 4) Calcul des dégats résiduels (= blessures à transférer au prochain tour)
    defender.residualDamage = sommeDegats - victims * defPV
    # 5) Calcul des individus à terre chez les defenseurs
    defender.group.groupMemberInjured += victims
    defender.group.groupMemberHealthy -= victims

    # On décompte les victimes
    if( victims == 0 ):
        addLog( 'logNormal' , 'Les défenseurs encaissent l\'assaut sans faiblir. Seuls quelques blessures légères ({} points de dégats) sont a déplorer'
                .format( defender.residualDamage ))
    elif( ( defender.group.groupMemberHealthy > 0 ) and ( defender.residualDamage > 0 ) ):
        addLog( 'logNormal' , '{} défenseurs tombent sous les coups des assaillants. De plus, quelques blessures légères ({} points de dégats) sont a déplorer'
                .format( victims, defender.residualDamage ))
    else:
        addLog( 'logNormal' , '{} défenseurs tombent sous les coups des assaillants.'
                .format( victims ))

    addLog( 'logNormal' , '{} combattants ont été mis à terre chez les défenseurs : il reste {} membres aptes à continuer la bataille'
                .format( defender.group.groupMemberInjured , defender.group.groupMemberHealthy ) )

###############################################################################
# Cette fonction réalise l'attaque d'un groupe par un autre et retourne les
# degats actuels du défenseurs
###############################################################################
# def phaseMorale():
    # On extrait le moral de chaque groupe

###############################################################################
# Phase de maintenance : on checke l'état des deux groupes
###############################################################################
def phaseMaintenance(groupBattleA , groupBattleB):
    # Check des faits suivants :
    ## Les groupes doivent avoir des membres en combat
    ## Les groupes ne doivent pas être démoralisés
    if ( ( groupBattleA.group.groupMemberHealthy < 1 ) and ( groupBattleB.group.groupMemberHealthy > 0 ) and ( groupBattleA.won is False ) and ( groupBattleB.won is False ) ):
        addLog( 'logNormal' , 'C\'est une belle victoire de {}, dont {} combattants restent valides !'
                    .format( groupBattleB.group.groupName , groupBattleB.group.groupMemberHealthy ))
        groupBattleB.won = True
    elif ( ( groupBattleB.group.groupMemberHealthy < 1 ) and ( groupBattleA.group.groupMemberHealthy > 0 ) and ( groupBattleA.won is False ) and ( groupBattleB.won is False ) ):
        addLog( 'logNormal' , 'C\'est une belle victoire de {}, dont {} combattants restent valides !'
                    .format( groupBattleA.group.groupName , groupBattleA.group.groupMemberHealthy ))
        groupBattleA.won = True
    elif ( ( groupBattleB.group.groupMemberHealthy < 1 ) and ( groupBattleA.group.groupMemberHealthy < 1 ) and ( groupBattleA.won is False ) and ( groupBattleB.won is False ) ):
        addLog( 'logNormal' , 'La bataille se solde par une débandade générale ! Les deux groupes sont épuisés et blessés. Pas de gagnant.' )
        groupBattleA.won = True
        groupBattleB.won = True
    else:
        addLog( 'logNormal' , 'Le groupe \"{}\" ({} , {} , {}) continue le combat contre \"{}\" ({} , {} , {} )'
                    .format(groupBattleA.group.groupName , groupBattleA.group.groupMemberHealthy, groupBattleA.group.groupMemberInjured , groupBattleA.group.groupMemberDead , groupBattleB.group.groupName , groupBattleB.group.groupMemberHealthy , 
                        groupBattleB.group.groupMemberInjured , groupBattleB.group.groupMemberDead ))


###############################################################################
# Cette fonction gère l'ajout d'une ligne à un compte rendu
# Elle gère aussi l'ajout de brackets HTML pour la mise en forme du log
# au niveau du template django
# loglevel is either logTitle, loglogSubTitle or logNormal
###############################################################################
def addLog( logLevel , strToAdd ):
    global battleLog
    battleLog = battleLog + '<p id=\"{}\">'.format(logLevel) +  strToAdd + '</p>' + '\n'
