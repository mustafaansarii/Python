def greattrethan(num):
    if num>5:
        return  True
    else:
        return  False

g10=lambda  num:num>10

l=[11,2,31,41,51,5,6,77]
print(list(filter(greattrethan,l)))
print(list(filter(g10,l)))