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
sieges_restants = 0

q_electoral = 100/6 #16.67

def imprime_statuts_temporaires_HARE(p):                    
    print("\n HARE Nombre de voix basé surle quotient électoral - " + str(nb_sieges) + " sièges à attribuer")
    print("_____________________________________________________________________________________" )
    print("\t Parti \t Voix \t Sièges Élus \t Attrib. \t Restes à calculer") 
    for i in p.keys():
        print("\t {0} \t {1} \t {2} \t\t {3} \t{4} ".format(i, p[i]['Voix'], q_entier_retourne_sieges(p[i]['Voix'],q_electoral), p[i]['sieges_d'], plus_fort_reste(p[i]['Voix'],q_electoral)))

def imprime_statuts_finaux_HARE(p):
    print("\n Nombre de voix basé surle quotient électoral avec siège restants attribués selon QUOTIENT DE HARE" )
    print("_____________________________________________________________________________________" )
    print("\t Parti \t Voix \t Sièges Élus \t Sièges Dist. \t\t Total")  
    for i in p.keys():
        print("\t {0} \t {1} \t\t {2} \t\t {3} \t\t {4}  ".format(i, p[i]['Voix'], p[i]['sieges_e'], p[i]['sieges_d'], p[i]['sieges_e'] + p[i]['sieges_d']))  

def imprime_statuts_temporaires_HONDT(p):                    
    print("\n HONDT Nombre de voix basé surle quotient électoral - " + str(nb_sieges) + " sièges à attribuer")
    print("_____________________________________________________________________________________" )
    for i in p.keys():
         print (p[i])
def imprime_statuts_finaux_HONDT(p):                    
    print("\n HONDT Nombre de voix basé surle quotient électoral - " + str(nb_sieges) + " sièges à attribuer")
    print("_____________________________________________________________________________________" )

    for i in p.keys():
         print (p[i])

def imprim_resu_HARE():
    print("\n Jefferson/Hondt:  Nombre de voix basé surle quotient électoral avec siège restants attribués selon QUOTIENT DE HARE" )
    print("_____________________________________________________________________________________" )
    print("\t Parti \t Voix \t Sièges Élus \t Sièges dist \t\t Total") 


# pour chaque parti, diviser le nb de voix obtenues par le quotient_electoral

#cherche la prochaine val max sans siege distribué
def get_max_quot_HARE(p, item):
    max_reste = 0
    for i in p.keys():
        if p[i][item] > max_reste and p[i]['sieges_d'] == 0:#on ne compte plus ceux qui ont déjà gagné par attribution
            max_reste = p[i][item]
    return max_reste

def get_max_quot_HONDT(p, item):
    max_q = 0
    for i in p.keys():
        if p[i][item] > max_q:
            max_q = p[i][item]
    return max_q

def q_entier_retourne_sieges(voix, q_electoral):  
    return voix//q_electoral

def plus_fort_reste(voix, q_electoral):
    return(voix % q_electoral)
 
# je fais 2 choses ici: calculer les sieges restants et attribuer selon max reste.
def resoudre_derniers_sieges(p):
    sieges_restants = nb_sieges
    
    for i in p.keys():
        sieges_restants -= p[i]['sieges_e']
        p[i]['sieges_d'] = 0
        
    while sieges_restants != 0:
        max = get_max_quot_HARE(p,'restes')
        for i in p.keys():
            if p[i]['restes'] == max:
                p[i]['sieges_d'] = 1
                sieges_restants -= 1
                break
        imprime_statuts_temporaires_HARE(p)    
    return p

def affecte_sieges_elus_et_restes(p):
    for i in p.keys():
        p[i]['sieges_e'] = q_entier_retourne_sieges(p[i]['Voix'],q_electoral)
        p[i]['restes'] = plus_fort_reste(p[i]['Voix'],q_electoral)
    return p


#fonction qui est rappelée tq il y a des sièges à attribuer
# je nomme les cles et items de fa]on dyamique avec num de la passe 
def siege_residuel_tous_partis(p):
#tous les sieges en jeu - sieges remportes par quotient electoral    
    sieges_restants = nb_sieges
    for i in p.keys():
        sieges_restants -= p[i]['sieges_e']
    print(sieges_restants)
  
    passe_repart = 1
    while sieges_restants != 0: 
        champ_repart =  'sieges_d' + str(passe_repart)
        q_a_verif = 'q' + str(passe_repart)
        max_q = get_max_quot_HONDT(p,q_a_verif,champ_repart)
        for i in p.keys():
             if p[i][q_a_verif] == max_q:
               p[i][champ_repart] = 1 
               sieges_restants -= 1
               break
        return p          
  
def repartition_sieges(p):   
    sieges_restants = nb_sieges
    passe_repartition = 2
    for i in p.keys():
        sieges_restants -= p[i]['sieges_e']
        p[i]['sieges_d1'] = 0
    
    siege_residuel_tous_partis(p)



#les passes subséquentes de calcul des quotients doivent tenir compte des nouveaux sieges attribués siege_dx
def affecte_sieges_elus(p):#nb de la passe
    for i in p.keys():
        p[i]['sieges_e'] = q_entier_retourne_sieges(p[i]['Voix'],q_electoral)
        p[i]['sieges_d'] = 0
    return p

def calcule_quotients(p, passe):# passe pour dynamiquement affecter champ siege_x si le quotient a gagné
    #TODO maintenir une liste du vainqueur du dernier siege car so diviseur = sieges_e +=2
    champ_q = 'q' + str(passe)
    for i in p.keys():
        if p[i]['sieges_e'] != 0: 
            p[i][champ_q] = p[i]['Voix'] / p[i]['sieges_e'] 
    return p                    

def init_methode_HARE():
    partis = {'A': {'Voix' : 42},'B': {'Voix' : 31}, 'C': { 'Voix' : 15}, 'D': { 'Voix' : 12}}
    p1 = affecte_sieges_elus_et_restes(partis)
 #   imprime_statuts_temporaires_HARE(p1)
    p2 = resoudre_derniers_sieges(p1)
    imprime_statuts_finaux_HARE(p2)
        

def siege_gagnant(p, num_q):
    global sieges_restants
    champ_q = 'q' + str(num_q)
    max_q = get_max_quot_HONDT(p,champ_q)
    
    for i in p.keys():
        if p[i][champ_q] == max_q:
            p[i]['sieges_d'] += 1
            sieges_restants = sieges_restants - 1
    return p

def c_sieges_restants(p):
    accu_sieges = 0
    for i in p.keys():
        accu_sieges += p[i]['sieges_e']
    return nb_sieges - accu_sieges
  
  

init_methode_HARE()    
    
    
    
    
    
    
    
    