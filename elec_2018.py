# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:58:36 2019

@author: jk
"""
#total du vote = 4 099 623
#bulletins valides 4 033 538

import re
import csv

total_votants = 4099623
q_electoral = 4099623/125
sieges_restants = nb_sieges = 125

def lecture_fich():
    le_sommaire = {}
    sieges = 0
    with open('elect_2018.csv', encoding="ISO-8859-1") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')      
        line_count = 0
        for row in csv_reader:
            if row[4] == '\xa0' or row[4] == '':
                sieges = 0
            else:
                sieges = int(row[4])
            le_sommaire[line_count+1] = {'parti':re.search(r'[(](.*)[)]',row[0]).group(1),'voix': int(row[1]),'sieges':sieges}
            line_count += 1
    return le_sommaire
    
def affecte_sieges_elus_et_restes(p):
    global sieges_restants
    for i in p.keys():
        p[i]['sieges_e'] = int(p[i]['voix']/q_electoral)
        sieges_restants -= p[i]['sieges_e']
        p[i]['restes'] = round(p[i]['voix'] % q_electoral,3)
    return p    

def imprime_statuts_temporaires_HARE(p):                    
    print("\n HARE Nombre de sieges supp. basé sur surle plus grand quotient électoral - " + str(nb_sieges) + " sièges à attribuer")
    print("_____________________________________________________________________________________" )
    for i in p.keys():
         print (str(i) + " " + str(p[i]))
    print("_____________________________________________________________________________________" )

def imprime_statuts_finaux_HARE(p):
    global total_votants                
    global nb_sieges                
    print("\n HARE Nombre de sieges supp. basé sur le plus grand quotient électoral - " + str(nb_sieges) + " sièges à attribuer")
    print("_____________________________________________________________________________________" )
    for i in p.keys():
         print (str(i) + " " + str(p[i].get('parti')) + " sieges: " + str(p[i].get('sieges')) +
                " v. " + str(p[i]['sieges_e']+ p[i]['sieges_d']) + " stats: % votes = " +
                str( 100* round(p[i]['voix']/total_votants,4))[:5] + " | sieges av. = %" +
                str(100 * round(p[i]['sieges']/nb_sieges,4))[:5]  + " | sieges ap. = %" + str((100 * round((p[i]['sieges_e']+
                   p[i]['sieges_d'])/nb_sieges,5)))[:5])
    print("_____________________________________________________________________________________" )


def resoudre_derniers_sieges(p):
   global sieges_restants
   for i in p.keys():
       p[i]['sieges_d'] = 0
        
   while sieges_restants != 0:
           max = get_max_quot_HARE(p,'restes')
           for i in p.keys():
               if p[i]['restes'] == max:
                   p[i]['sieges_d'] = 1
                   sieges_restants -= 1
                   break    
   return p

def get_max_quot_HARE(p, item):
    max_reste = 0
    for i in p.keys():
        if p[i][item] > max_reste and p[i]['sieges_d'] == 0:#on ne compte plus ceux qui ont déjà gagné par attribution
            max_reste = p[i][item]
    return max_reste

def affecte_sieges_elus(p):#nb de la passe
    for i in p.keys():
        p[i]['sieges_e'] = round(p[i]['voix']/q_electoral, 2)
        p[i]['sieges_d'] = 0 #ce champ accumulera les sieges distribués selon formules
    return p

def c_sieges_d_a_repartir(p):
    global nb_sieges
    global sieges_restants
    accu_sieges = 0
    for i in p.keys():
        accu_sieges += int(p[i]['sieges_d']) + int(p[i]['sieges_e'])
    sieges_restants = nb_sieges - accu_sieges 
    return sieges_restants

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
        p[i][champ_q] = round(p[i]['voix'] / (sieges + 1 + tour_precedent),2)
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

def get_max_quot_HONDT(p, item):
    max_q = 0
    for i in p.keys():
        if p[i][item] > max_q:
            max_q = p[i][item]
    return max_q

def imprime_statuts_finaux_HONDT(p):                    
    accu_sieges = 0
    print("\n HONDT Nombre de voix basé surle quotient électoral - " + str(nb_sieges) + " sièges à attribuer")
    print("_____________________________________________________________________________________" )
    for i in p.keys():
        accu_sieges = int(p[i]['sieges_e']) + int(p[i]['sieges_d']) 
        print (str(i) + " " + str(p[i]) + " Total = " + str(accu_sieges))
        accu_sieges = 0
    print("Sièges restants = " + str(sieges_restants))
    
def imprime_stats_HONDT(p):                    
    accu_sieges = 0
    print("\n HONDT Nombre de voix basé surle quotient électoral - " + str(nb_sieges) + " sièges à attribuer")
    print("_____________________________________________________________________________________" )
    for i in p.keys():
        accu_sieges = int(p[i]['sieges_e']) + int(p[i]['sieges_d']) 
        print (str(i) + " " + str(p[i]['parti']) + " | sieges_av : " + str(p[i]['sieges']) +  " | sieges_ap : " + str(int(p[i]['sieges_e'])) + " Total = " + str(accu_sieges))
        accu_sieges = 0
    print("Sièges restants = " + str(sieges_restants))

def init_HARE():    
    d = lecture_fich()
    d2 = affecte_sieges_elus_et_restes(d)
    
#    imprime_statuts_temporaires_HARE(d2)
    
    d3 = resoudre_derniers_sieges(d2)
    
 #   imprime_statuts_temporaires_HARE(d3)
    imprime_statuts_finaux_HARE(d3)

def init_HONDT():
    passe = 1
    partis = lecture_fich()
    p1 = affecte_sieges_elus(partis)
#   
#    imprime_statuts_temporaires_HONDT(p4, passe)
    
    while c_sieges_d_a_repartir(p1) > 0:
        p2 = calcule_quotients(p1, passe)
        calcule_q_gagnant(p2, passe)
        p1 = p2   
        passe += 1
 #   imprime_statuts_finaux_HONDT(p1)
    imprime_stats_HONDT(p1)

init_HARE()
init_HONDT()


