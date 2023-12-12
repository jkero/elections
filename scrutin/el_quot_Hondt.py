# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 09:20:25 2019

@author: jk
"""

# inspiré de https://fr.wikipedia.org/wiki/Scrutin_proportionnel_plurinominal#M%C3%A9thode_d'Hondt

#quotient électoral = nombre de votes divisé par nb sièges.
# exmple 100 votes pour 4 partis
# on assume au moins 5% de représentativité pour les partis inscrits

nb_partis = 4
nb_votes = 100
nb_sieges = 6
sieges_restants = 6

q_electoral = nb_votes/nb_sieges 


def imprime_statuts_temporaires_HONDT(p,passe):                    
    print("\n HONDT Nombre de voix basé surle quotient électoral - " + str(nb_sieges) + " sièges à attribuer")
    print("_____________________________________________________________________________________" )
    for i in p.keys():
         print (str(i) + " " + str(p[i]))
    print("Sièges restants = " + str(sieges_restants) + " tour = " + str(passe))
    
def imprime_statuts_finaux_HONDT(p):                    
    accu_sieges = 0
    print("\n HONDT Nombre de voix basé surle quotient électoral - " + str(nb_sieges) + " sièges à attribuer")
    print("_____________________________________________________________________________________" )
    for i in p.keys():
        accu_sieges = int(p[i]['sieges_e']) + int(p[i]['sieges_d']) 
        print (str(i) + " " + str(p[i]) + " Total = " + str(accu_sieges))
        accu_sieges = 0
    print("Sièges restants = " + str(sieges_restants))
# pour chaque parti, diviser le nb de voix obtenues par le quotient_electoral

#cherche la prochaine val max sans siege distribué


def get_max_quot_HONDT(p, item):
    max_q = 0
    for i in p.keys():
        if p[i][item] > max_q:
            max_q = p[i][item]
    return max_q
 
#les passes subséquentes de calcul des quotients doivent tenir compte des nouveaux sieges attribués siege_dx
def affecte_sieges_elus(p):#nb de la passe
    for i in p.keys():
        p[i]['sieges_e'] = round(p[i]['Voix']/q_electoral, 2)
        p[i]['sieges_d'] = 0 #ce champ accumulera les sieges distribués selon formules
    return p

def calcule_quotients(p, passe):# passe pour dynamiquement affecter champ siege_x si le quotient a gagné
    #a la base, le quotient est nb de sieges elus + 1
    #si le parti a gagné un tour précédent le diviseur = sieges_e + 1 + siege_d
    champ_q = 'q' + str(passe)
    tour_precedent = 0
    for i in p.keys():
        sieges = int(p[i]['sieges_e'])
        #si ce parti a gagné le tour precedent alors div += 1 je detecte avec q-1
        if passe > 1 and p[i]['dernier_tour'] != 0:
            tour_precedent = int(p[i]['sieges_d'])
        #if sieges != 0:
        p[i][champ_q] = round(p[i]['Voix'] / (sieges + 1 + tour_precedent),2)
        tour_precedent = 0
    return p                    

def calcule_q_gagnant(p, num_q):
    global sieges_restants
    champ_q = 'q' + str(num_q)
    max_q = get_max_quot_HONDT(p,champ_q)
    
    for i in p.keys():
        if p[i][champ_q] == max_q:
            p[i]['sieges_d'] += 1
            p[i]['dernier_tour'] = num_q #indicateur pour ajouter 1 ou non au quotient
            sieges_restants -= 1
        elif not p[i].get('dernier_tour'):
            p[i]['dernier_tour'] = 0
    return p

def c_sieges_d_a_repartir(p):
    global nb_sieges
    global sieges_restants
    accu_sieges = 0
    for i in p.keys():
        accu_sieges += int(p[i]['sieges_d']) + int(p[i]['sieges_e'])
    sieges_restants = nb_sieges - accu_sieges 
    return sieges_restants
  

def init_methode_HONDT():
    passe = 1
    partis = {'A': {'Voix' : 42},'B': {'Voix' : 31}, 'C': { 'Voix' : 15}, 'D': { 'Voix' : 12}}  
    p1 = affecte_sieges_elus(partis)
#   
#    c_sieges_d_a_repartir(p1)
#    imprime_statuts_temporaires_HONDT(p1, passe)
#    
#    
#    passe = 1
#    p2 = calcule_quotients(p1, passe)
#    calcule_q_gagnant(p2, passe)
#    c_sieges_d_a_repartir(p2)
#    
#    imprime_statuts_temporaires_HONDT(p2, passe)
#    
#    passe = 2
#    p3 = calcule_quotients(p2, passe)
#    calcule_q_gagnant(p3, passe)
#    c_sieges_d_a_repartir(p3)
#    
#    imprime_statuts_temporaires_HONDT(p3, passe)
#    
#    passe = 3
#    p4 = calcule_quotients(p3, passe)
#    calcule_q_gagnant(p4, passe)
#    c_sieges_d_a_repartir(p4)
#    
#    imprime_statuts_temporaires_HONDT(p4, passe)
    
    while c_sieges_d_a_repartir(p1) > 0:
        p2 = calcule_quotients(p1, passe)
        calcule_q_gagnant(p2, passe)
        p1 = p2   
        passe += 1
    imprime_statuts_finaux_HONDT(p1)
 
#    cpt = nb_sieges - c_sieges_restants(p1)
#    while cpt != 0:
 #   p2 = calcule_quotients(p1, passe)
 #   imprime_statuts_temporaires_HONDT(p2)
#        p3 = siege_gagnant(p2,passe)
##    p3 = repartition_sieges(p2)

#        passe += 1
#        cpt -= 1
   
if __name__ == "__main__":
    init_methode_HONDT()
    
    
    
    
    
    
    
    