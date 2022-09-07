import sys
import pandas as pd

ruta= sys.argv[1] #primer elemento de la comanda desde el terminal
print(ruta)

df = pd.read_excel (r'{ruta}')
print (df)
