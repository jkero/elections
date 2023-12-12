import json
import pandas as pd
from io import StringIO

df1 = pd.read_json('../resultats.json',lines=True, orient="columns")
#df1.set_index('statistiques', inplace=True)# statistiques ou circonscriptions
print(df1['statistiques'][0])

for v in df1['statistiques']:
    print(type(v))
    for k, vv in v.items():
        print(f"\nKey: {k}")
        print(f"Value: {vv}\n")
        print(f"Type: type({vv})")

    """
    Pour les recherches des modes électoraux
    on a besoin de:
    
    nbVoteTotal par parti
    nbVoteExerce
    nbVoteValide
    
        
    """


