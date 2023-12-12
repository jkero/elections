# canevas automatique avec dessin de carres pour representer des blocs
# y = colonnes
# x = rangees

x = 3
y = 4
blocW = 20
bloch = 20
bloc = []

for i in range (0, x*y):
    bloc.append({i*20, i + 20})
    if i % y == 0:
        print(i)
        print("\n")
    else:
        print(i)
        
print (bloc)
   