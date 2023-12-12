'''1° un siège de région est accordé à chacune des 16 régions, autres que celle
du Nord-du-Québec;
2° les 29 sièges de région restants sont répartis comme suit :
a) pour chacune des 17 régions, le nombre total d’électeurs de cette région
selon la liste électorale permanente est successivement divisé par les diviseurs 1,
2, 3, 4, 5 et ainsi de suite, de manière à obtenir les quotients qui correspondent
à chacun de ces diviseurs;
b) le calcul de ces quotients est effectué jusqu’à ce que les 29 quotients les
plus élevés, pour l’ensemble des régions, aient été obtenus;
c) chacun des 29 quotients ainsi obtenus est retenu et est associé à la région
qui y correspond;
d) le nombre de sièges de région supplémentaires accordés à une région est
égal au nombre de quotients qui lui est ainsi associé. ».

'''# -*- coding: utf-8 -*-
import csv


def tri_par_sous_liste(liste, index_quot):
    ss = []
    temp_region = ''
    temp_max_region = 0
#    print(len(liste))
    for i in range(len(liste)):
        ss = liste[i][5]
        if ss and len(ss) >= index_quot+1:
            if ss[index_quot] > temp_max_region:
                temp_max_region = ss[index_quot]
                temp_region = liste[i][1]
    print("passe index " + str(index_quot) + " = " +  temp_region + " : " + str(temp_max_region))
   
  


#REQUIERT UN CSV TRIÉ PAR RÉGIONS ADMIN
def diviseurs(pop):
    resu = []
    for i in range(2,400):
        c = pop/i
        for j in range(2,50000):
           # print(c)
            if c == j:               
              resu.append(c)
#              print(str(c)+ " == " + str(j))             
    resu.sort()
    resu.reverse()
    return resu

def swap(liste, x, y):
    buf = []
    buf = liste[x]
    liste[x] = liste[y]
    liste[y] = buf
    return list


def tri_stat_pop_quot(liste):
#    print ("========================AVANT============")
    
#    for i in range(len(liste)):
#        print(liste[i])
    for i in range(len(liste)):      
        for j in range(i+1,len(liste)):
            if liste[i][4] > liste[j][4]:
                swap(liste,i,j)  
 #   print ("========================APRES============")
#    for j in range(len(liste)):
#        print(liste[j])
    print(len(liste))  
    return liste
#    print(liste)
  
# retourne une liste des régions/circonscription pop par region et diviseur
# de region; la liste est triée par la valeur du rapport pop de région sur nb de circonscription(diviseur)       

def lecture_fich():
    la_liste = []   
    la_liste_stat = []
    with open('../circonscriptions_regios_orig.csv', encoding="ISO-8859-1") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')      
        line_count = 0
        pop_cpt_region = 0
        region_prev = ''
        diviseur = 0 #le nb de circonscriptions détecté par changement de region
        votes = 0
        for row in csv_reader:
            if line_count == 0:
#                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
     #           print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
#                print(f'\t{row[1]} {row[9]}')
                
                region = row[0] 
                if line_count == 1:                    
                     diviseur = 0
                circ = row[2]
                votes = int(row[10])
                if region != region_prev and line_count > 1:
        #            print("\n ++++++++++++++++++++++++++++++++++++-" + region_prev)
                    la_liste_stat.append(["TOTAL ", region_prev, pop_cpt_region, diviseur, int(pop_cpt_region/diviseur)])
                    pop_cpt_region = votes
                    diviseur = 1
                    
        #            print("\n -----------------------------------" + region)
                else:
                    pop_cpt_region += votes
                    diviseur += 1
                la_liste.append([region, circ, votes])
                line_count += 1
                region_prev = region

#       traiter les accus da la dernière ligne du reader                
        la_liste_stat.append(["TOTAL ", region_prev, pop_cpt_region, diviseur, int(pop_cpt_region/diviseur)])


#        print (la_liste)
#        print (la_liste_stat)
#        print("***************test***************")
#        print (max(la_liste_stat))
#        print("***************test***************")
        return la_liste_stat

if __name__ == "__main__":
    l = lecture_fich()
    stat = tri_stat_pop_quot(l)

    #ajout des sous-listes des quotients entiers à la fin des enr. des régions
    # pas clair si les plus gros quotients vont déterminer le siege électoral
    for i in range(len(stat)):
         dd = diviseurs(stat[i][4])
         stat[i].append(dd)
    print("***************  PAR POP/CIRC ***************")
    #print résultat
    for j in range(len(stat)):
        print(stat[j])

    #trier les résu selon plus grosse liste quotients TODO comment on compare ça ?
    for i in range(len(stat)):
        for j in range(i+1,len(stat)):
            if stat[i][5] > stat[j][5]:
                swap(stat,i,j)
    print("***************  PAR LISTE DIVISEURS le plus haut en premier ?? ***************")
    #trier âr plus grossse sours liste de quotients... ???
    stat.reverse()
    for j in range(len(stat)):
        print(stat[j])

    #comparaison de chaque index de chaque sous-chaine -> plus grabd gagne
    for i in range(25):
        tri_par_sous_liste(stat,i)


    #        ss = stat[j][5]

    #        print(str(j) + "-- " + str(len(ss)))
            #tri_par_sous_liste(stat,i)

        
        
        
        
        
        
        
        
        
        
        
        
        
        