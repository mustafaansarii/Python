from collections import  namedtuple
a=namedtuple("name","tech")
s= a._make(["ai","technology"])
print(s)