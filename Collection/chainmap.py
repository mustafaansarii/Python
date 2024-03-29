from collections import ChainMap

a= {1: "edureka", 2:"python"}
b={3:"Ml",4:"AI"}
a1= ChainMap(a,b)
print(a1)