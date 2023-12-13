Les types d'élections [1]_
===========================

Démocratie, systèmes électoraux [2]_ , etc.
+++++++++++++++++++++++++++++++++++++++++++

Ce texte s'intéresse aux scrutins et à la représentativité électorale pour des systèmes démocratiques.


.. todo::

    définir *scrutin uninominal*, *scrutin proportionnel plurinominal* (ou *représentation proportionnelle à scrutin de liste*), *Scrutin majoritaire plurinominal*, et les variantes.

.. todo::

    expliquer les méthodes de répartition des sièges, comme *plus fort reste* (Hare, Droop), *plus forte moyenne* (Jefferson/Hondt) et modes de calculs (Adams, Sainte-Lagüe).

.. todo::

    expliquer le seuil de représentativité (tous les modes de scrutin) : pourcentage des voix obtenues, ou alors des inscrits (?) ou même en sièges obtenus. Les frais de campagne peuvent être remboursés si ce seuil est franchi.

Lexique
+++++++

.. list-table:: Lexique (Élections Canada)

    * -  Abbréviation
      -  Nom complet
      -  Description
    * -  SMU
      -  Scrutin majoritaire uninominal
      -  Le pays est divisé en circonscriptions uninominales. L'électeur choisit l'un des candidats inscrits sur le bulletin de vote. Le candidat qui remporte plus de voix que tout autre obtient le siège.
    * -  VUT
      -  Vote unique transférable
      -  Le pays est divisé en circonscriptions plurinominales. L'électeur classe certains ou l'ensemble des candidats sur son bulletin de vote. On calcule un quota (méthode Hare ou Droop) en fonction des
         votes valides et l'on compte les voix de premier choix accordées aux candidats.
         Les candidats qui obtiennent plus de voix de premier choix que les quotas sont élus, et les voix excédentaires sont redistribuées entre les candidats inscrits en deuxième place. Le décompte se poursuit ainsi
         par élimination des derniers candidats et redistribution complète des voix excédentaires des gagnants, jusqu'à ce que tous les sièges soient attribués.
    * -  VUNT
      -  Vote unique non transférable
      -  Comme le VUT, mais les électeurs ne votent qu'une fois (au lieu d'un maximum d'une fois par siège disponible).
    * -  \-
      -  Scrutin de liste
      -  Le pays est divisé en circonscriptions plurinominales (ou est désigné comme une seule circonscription plurinominale). Chaque parti dresse une liste de candidats sur les bulletins de vote, et les électeurs
         choisissent l'une de ces listes. Les listes peuvent être ouvertes (l'électeur peut exprimer une préférence parmi les candidats du parti pour lequel il vote) ou fermées (un seul vote pour un parti). Les sièges sont
         attribués selon une formule de la moyenne la plus élevée ou du résiduel le plus important. Une fois calculé le nombre de sièges de chaque parti, les sièges sont attribués aux candidats qui se trouvent en tête de liste.
    * -  SMM
      -  Scrutin majoritaire mixte
      -  Chaque électeur vote deux fois : une fois pour le candidat d'une circonscription à SMU et une fois pour la liste de parti. Dans le cadre du SMM complémentaire, on calcule le nombre de sièges de chaque parti
         en fonction du nombre de voix obtenues par les listes, puis on en retranche les sièges obtenus dans le cadre du SMU pour déterminer les sièges auxquels chaque parti a droit dans le cadre du scrutin de liste. Dans le
         cadre du SMM parallèle, les deux groupes de députés sont élus séparément, et leurs totaux combinés servent à attribuer les sièges à chaque parti.

Autres définitions
------------------
.. glossary::

    **Quotient électoral** :
        Total des votes / total des sièges à pourvoir. Ça donne un nombre qui serait la représentation idéale (surtout dans un contexte de scrutin proportionnel) de votes pour chaque siège. À moins de n'obtenir aucun
        siège (le nb de votes est plus petit que le quotient électoral), chaque parti compte le nombre de voix reçues et le divise par le quotient pour obtenir le nombre de sièges remportés (v/(v/s) = s).

        Exemple:  5 sièges à pourvoir, 100 votants. Q = 20 et n partis. Parti X obtient 29 votes : 29 / 20 = 1 siège remporté (les autres partis font le même calcul). Comme la division produit aussi un reste (29/20 = 1,45),
        le total de ces restes pour chaque parti représente des votes (et des sièges) qui doivent être répartis, selon différentes méthodes. Pour la méthode de Hare, la répartition se fait selon le plus grand reste : tant qu'il y
        a des sièges à répartir on procède en attribuant un siège aux partis avec les plus grand restes (en ordre de grandeur). Des partis ayant manqué le quotient de peu peuvent se voir attribuer un siège supplémentaire, ce qui
        améliore leur représentativité.

        La valeur de l'écart de représentation, % des sièges remportés - % des voix remportées peut être un indice de la représentation réelle. Ainsi par exemple un parti ayant 30% des voix et 40% de sièges a un écart de -10%, le négatif indique une sur-représentation.

Notes
-----

Graphes: répartition de Hare (Quotient de Hare)

.. uml::

    @startuml
        start
        note right
        s = nombre de sièges à attribuer
        vt = nb votes total
        vp = votes pour un parti **x**
        q est le quotient électoral vt/s
        end note
        if (scrutin proportionnel?) then (oui)
            :obtenir total votes (vt) et total sièges (s);
            : calculer quotient q = (vt/s);
            : répartir le vote (sièges restants)
              selon les restes de vp/q;
        note right
            Hare: la valeur la plus haute des
            restes remporte le premier siège,
            et ainsi de suite pour les suivantes.
        end note
        else (non)
            :le quotient n'est pas utile pour
            calculer une répartition;
            note right
                Si le mode de scrutin n'est
                pas proportionnel il n'y a pas
                de répartition autre que celle
                décidée par la carte électorale
                (dans le cas de circonscriptions
                ou autres divisions).
            end note
        endif
        stop
    @enduml



.. [1]  https://www.elections.ca/content.aspx?section=res&dir=eim/issue1&document=p5&lang=f (Perspectivs électorales juin 1999)

        https://fr.wikipedia.org/wiki/Scrutin_proportionnel_plurinominal

        MacIvor, Heather, *Système électoral proportionnel ou semi-proportionnel : effets possibles sur la politique canadienne* , 1999: https://www.elections.ca/res/rec/fra/sys/macivor_f.pdf

        https://publications.gc.ca/Collection-R/LoPBdP/BP/bp334-f.htm#1.%20Le%20scrutinmajoritairetourtxt

.. [2] O'Neal, Brian, *Les systèmes électoraux*, Division des affaires politiques et sociales, Mai 1993 (BP-334F)